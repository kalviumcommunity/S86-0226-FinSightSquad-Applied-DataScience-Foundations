"""
data_cleaning.py
----------------
Handles all data preprocessing steps:
  - Date parsing and normalisation
  - Amount handling (sign convention, numeric coercion)
  - Text normalisation for descriptions
  - Duplicate detection and removal
  - Missing value imputation
"""

import pandas as pd
import numpy as np


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run the full cleaning pipeline on the raw transaction DataFrame.

    Steps applied (in order):
    1. Strip whitespace from all string columns.
    2. Parse and normalise the date column.
    3. Coerce the amount column to numeric.
    4. Normalise the transaction_type column.
    5. Derive signed amount (negative = expense, positive = income).
    6. Normalise description text.
    7. Remove exact duplicate rows.
    8. Drop rows with critical missing values.

    Parameters
    ----------
    df : pd.DataFrame
        Raw DataFrame returned by data_loader.load_transactions().

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with additional helper columns:
        ``month``, ``year``, ``month_label``, ``signed_amount``.
    """
    df = df.copy()

    # ── 1. Strip whitespace ────────────────────────────────────────────────────
    df = _strip_whitespace(df)

    # ── 2. Parse dates ─────────────────────────────────────────────────────────
    df = _parse_dates(df)

    # ── 3. Coerce amounts ──────────────────────────────────────────────────────
    df = _coerce_amounts(df)

    # ── 4. Normalise transaction type ─────────────────────────────────────────
    df = _normalise_transaction_type(df)

    # ── 5. Create signed amount (expenses are negative) ───────────────────────
    df = _create_signed_amount(df)

    # ── 6. Normalise descriptions ─────────────────────────────────────────────
    df = _normalise_descriptions(df)

    # ── 7. Remove duplicates ──────────────────────────────────────────────────
    df = _remove_duplicates(df)

    # ── 8. Drop rows missing critical values ──────────────────────────────────
    df = _drop_critical_nulls(df)

    # ── 9. Add temporal helper columns ────────────────────────────────────────
    df = _add_temporal_columns(df)

    print(f"[DataCleaner] Cleaned dataset: {len(df)} valid transactions remaining.")
    return df.reset_index(drop=True)


# ══════════════════════════════════════════════════════════════════════════════
# Private helper functions
# ══════════════════════════════════════════════════════════════════════════════

def _strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading/trailing whitespace from all object (string) columns."""
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()
    return df


def _parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse the ``date`` column to pandas datetime, handling multiple formats.
    Slash-based formats are parsed with dayfirst=True (common bank exports).
    Rows with unparsable dates are kept but flagged as NaT.
    """
    original_count = len(df)
    raw_dates = df["date"].astype(str).str.strip()

    parsed = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    slash_mask = raw_dates.str.contains("/", regex=False)

    if (~slash_mask).any():
        parsed.loc[~slash_mask] = pd.to_datetime(raw_dates.loc[~slash_mask], errors="coerce")

    if slash_mask.any():
        # DD/MM/YYYY (and DD/MM/YYYY HH:MM:SS) is common in bank exports.
        parsed.loc[slash_mask] = pd.to_datetime(
            raw_dates.loc[slash_mask],
            dayfirst=True,
            errors="coerce",
        )

    # Final fallback pass for any still-missing values.
    still_nat = parsed.isna()
    if still_nat.any():
        unresolved = raw_dates.loc[still_nat]
        unresolved_slash = unresolved.str.contains("/", regex=False)

        if unresolved_slash.any():
            parsed.loc[unresolved.index[unresolved_slash]] = pd.to_datetime(
                unresolved.loc[unresolved_slash],
                dayfirst=True,
                errors="coerce",
            )

        if (~unresolved_slash).any():
            parsed.loc[unresolved.index[~unresolved_slash]] = pd.to_datetime(
                unresolved.loc[~unresolved_slash],
                errors="coerce",
            )

    df["date"] = parsed
    unparsed = df["date"].isna().sum()
    if unparsed > 0:
        print(f"[DataCleaner] Warning: {unparsed}/{original_count} rows have unparsable dates.")
    return df


def _coerce_amounts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Coerce the ``amount`` column to float.
    Strips currency symbols ($, £, €) and commas before conversion.
    Rows that cannot be converted are set to NaN.
    """
    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace(r"[\$£€,]|Rs\.?\s*|INR\s*|₹\s*", "", regex=True)
        .str.strip()
    )
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    nan_count = df["amount"].isna().sum()
    if nan_count > 0:
        print(f"[DataCleaner] Warning: {nan_count} rows have non-numeric amounts — will be dropped.")
    return df


def _normalise_transaction_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardise ``transaction_type`` to lowercase 'debit' or 'credit'.
    Unrecognised values default to 'debit'. Column is created if absent.
    """
    if "transaction_type" not in df.columns:
        df["transaction_type"] = "debit"
        return df
    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"[_\-]+", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )

    # Expand common abbreviations and human-readable variants.
    _CREDIT_ALIASES = {
        "credit", "cr", "c", "in", "incoming", "income", "inflow",
        "deposit", "received", "receive", "salary", "refund", "cashback",
        "earning", "earnings", "revenue",
    }
    _DEBIT_ALIASES = {
        "debit", "dr", "d", "out", "outgoing", "outflow", "expense",
        "expenses", "spend", "spending", "purchase", "payment", "paid",
        "withdrawal", "withdraw", "transfer out", "sent",
    }

    def _map_tx_type(raw: str) -> str:
        if raw in _CREDIT_ALIASES:
            return "credit"
        if raw in _DEBIT_ALIASES:
            return "debit"
        # Handle noisy labels like "income credited" / "money outgoing".
        if any(tok in raw for tok in ["credit", "income", "incoming", "inflow", "deposit", "received"]):
            return "credit"
        if any(tok in raw for tok in ["debit", "expense", "spend", "outgoing", "outflow", "withdraw", "paid"]):
            return "debit"
        return ""

    mapped = df["transaction_type"].apply(_map_tx_type)
    valid = {"debit", "credit"}
    mask_invalid = ~mapped.isin(valid)
    if mask_invalid.sum() > 0:
        # Infer from amount sign where possible before defaulting to debit.
        inferred = np.where(df.loc[mask_invalid, "amount"] > 0, "credit", "debit")
        mapped.loc[mask_invalid] = inferred
        print(
            f"[DataCleaner] Warning: {mask_invalid.sum()} rows had unrecognised "
            "transaction_type — inferred using amount sign."
        )

    df["transaction_type"] = mapped
    return df


def _create_signed_amount(df: pd.DataFrame) -> pd.DataFrame:
    """
    Derive ``signed_amount``:
      - Credit (income)  → positive
      - Debit  (expense) → negative
    The raw ``amount`` column always stores the absolute value.
    """
    df["amount"] = df["amount"].abs()  # ensure raw amount is always positive
    df["signed_amount"] = np.where(
        df["transaction_type"] == "credit",
        df["amount"],
        -df["amount"],
    )
    return df


def _normalise_descriptions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the ``description`` field:
    - Convert to title case for readability.
    - Collapse multiple whitespace characters.
    - Replace NaN descriptions with 'Unknown'.
    Column is created with 'Unknown' if absent.
    """
    if "description" not in df.columns:
        df["description"] = "Unknown"
        return df
    df["description"] = (
        df["description"]
        .replace("nan", np.nan)
        .fillna("Unknown")
        .str.title()
        .str.replace(r"\s+", " ", regex=True)
    )
    return df


def _remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows that are exact duplicates across date, description,
    amount, and transaction_type (using whichever of those exist).
    """
    all_key_cols = ["date", "description", "amount", "transaction_type"]
    key_cols = [c for c in all_key_cols if c in df.columns]
    before = len(df)
    df = df.drop_duplicates(subset=key_cols, keep="first")
    removed = before - len(df)
    if removed > 0:
        print(f"[DataCleaner] Removed {removed} duplicate transactions.")
    return df


def _drop_critical_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows where critical columns (date, amount) are null.
    These rows are unrecoverable without the core fields.
    """
    before = len(df)
    df = df.dropna(subset=["date", "amount"])
    dropped = before - len(df)
    if dropped > 0:
        print(f"[DataCleaner] Dropped {dropped} rows with null date or amount.")
    return df


def _add_temporal_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add convenience temporal columns derived from ``date``:
    - ``year``        : integer year
    - ``month``       : integer month (1–12)
    - ``month_label`` : string 'YYYY-MM' for charting
    - ``week``        : ISO week number
    - ``day_of_week`` : day name (e.g. 'Monday')
    """
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_label"] = df["date"].dt.to_period("M").astype(str)
    df["week"] = df["date"].dt.isocalendar().week.astype(int)
    df["day_of_week"] = df["date"].dt.day_name()
    return df
