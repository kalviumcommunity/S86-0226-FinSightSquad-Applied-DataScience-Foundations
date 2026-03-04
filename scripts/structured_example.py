"""Structured example for the Code Organization milestone.

This script demonstrates a clean, readable layout:
- imports at the top
- constant configuration grouped together
- small focused helper functions
- a `main()` that coordinates work
- `if __name__ == "__main__"` guard for top-level execution

Run with:

    python scripts/structured_example.py

No external dataset is required — the script generates sample data.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from statistics import mean
from typing import List, Dict

# ---------------------
# Configuration / Constants
# ---------------------
SAMPLE_SIZE = 12
CURRENCY = "USD"


@dataclass
class Transaction:
    id: int
    amount: float
    date: datetime


# ---------------------
# Helper functions (small, focused)
# ---------------------
def generate_sample_transactions(n: int = SAMPLE_SIZE) -> List[Transaction]:
    """Generate a small list of sample Transaction objects."""
    now = datetime.utcnow()
    return [Transaction(id=i + 1, amount=round((i + 1) * 10.5, 2), date=now) for i in range(n)]


def compute_summary(transactions: List[Transaction]) -> Dict[str, float]:
    """Compute simple numeric summary for a list of transactions.

    Returns a dictionary with count, total, mean, min, max.
    """
    amounts = [t.amount for t in transactions]
    if not amounts:
        return {"count": 0, "total": 0.0, "mean": 0.0, "min": 0.0, "max": 0.0}

    return {
        "count": len(amounts),
        "total": sum(amounts),
        "mean": mean(amounts),
        "min": min(amounts),
        "max": max(amounts),
    }


def format_currency(amount: float, currency: str = CURRENCY) -> str:
    """Return a simple human-readable currency string."""
    return f"{currency} {amount:,.2f}"


def print_summary(summary: Dict[str, float]) -> None:
    """Nicely print the computed summary to stdout."""
    print("Transaction summary:")
    print(f"  Count: {summary['count']}")
    print(f"  Total: {format_currency(summary['total'])}")
    print(f"  Mean:  {format_currency(summary['mean'])}")
    print(f"  Min:   {format_currency(summary['min'])}")
    print(f"  Max:   {format_currency(summary['max'])}")


# ---------------------
# Main program flow (keeps top-level execution minimal)
# ---------------------
def main() -> None:
    """Main entry point: generate data, compute and print summary."""
    transactions = generate_sample_transactions()
    summary = compute_summary(transactions)
    print_summary(summary)


if __name__ == "__main__":
    main()
