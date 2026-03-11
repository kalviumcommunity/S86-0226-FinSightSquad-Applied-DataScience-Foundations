"""
histograms.py
---------------
Simple utility to create and save histogram visualizations for numeric columns.

Usage:
    python src/histograms.py --csv data/sample_01_standard.csv

Outputs are written to `outputs/histograms/` as HTML and PNG.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import pandas as pd
import plotly.express as px


OUT_DIR = Path("outputs/histograms")


def ensure_out():
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def numeric_columns(df: pd.DataFrame):
    return list(df.select_dtypes(include=["number"]).columns)


def make_histogram(df: pd.DataFrame, col: str, nbins: int = 50):
    fig = px.histogram(
        df, x=col, nbins=nbins, marginal="box",
        title=f"Histogram — {col}", labels={col: col},
    )
    fig.update_layout(showlegend=False)
    out_html = OUT_DIR / f"hist_{col}.html"
    out_png = OUT_DIR / f"hist_{col}.png"
    fig.write_html(out_html, include_plotlyjs="cdn")
    # requires kaleido in environment
    try:
        fig.write_image(str(out_png))
    except Exception:
        # If kaleido not installed or fails, skip PNG
        pass
    return out_html, out_png


def compare_by_category(df: pd.DataFrame, col: str, cat_col: str = "transaction_type"):
    if cat_col not in df.columns:
        return None
    fig = px.histogram(
        df, x=col, color=cat_col, barmode="overlay", nbins=60,
        title=f"Histogram — {col} by {cat_col}", labels={col: col, cat_col: cat_col},
        opacity=0.6,
    )
    fig.update_layout()
    out_html = OUT_DIR / f"hist_{col}_by_{cat_col}.html"
    out_png = OUT_DIR / f"hist_{col}_by_{cat_col}.png"
    fig.write_html(out_html, include_plotlyjs="cdn")
    try:
        fig.write_image(str(out_png))
    except Exception:
        pass
    return out_html, out_png


def summary_and_interpretation(df: pd.DataFrame, col: str) -> str:
    s = df[col].dropna()
    desc = s.describe()
    skew = s.skew()
    interp = []
    interp.append(f"Count: {int(desc['count'])}")
    interp.append(f"Mean: {desc['mean']:.2f}")
    interp.append(f"Median (50%): {desc['50%']:.2f}")
    interp.append(f"Std: {desc['std']:.2f}")
    interp.append(f"Skewness: {skew:.2f}")
    if skew > 1:
        interp.append("Distribution is strongly right-skewed (long right tail).")
    elif 0.5 < skew <= 1:
        interp.append("Distribution is moderately right-skewed.")
    elif -0.5 <= skew <= 0.5:
        interp.append("Distribution is approximately symmetric.")
    elif -1 <= skew < -0.5:
        interp.append("Distribution is moderately left-skewed.")
    else:
        interp.append("Distribution is strongly left-skewed (long left tail).")
    return "\n".join(interp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", default="data/sample_01_standard.csv")
    parser.add_argument("--nbins", type=int, default=50)
    parser.add_argument("--compare", action="store_true", help="Make comparison by transaction_type if available")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        raise SystemExit(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path, parse_dates=["date"] if "date" in pd.read_csv(csv_path, nrows=0).columns else None)

    ensure_out()

    num_cols = numeric_columns(df)
    if not num_cols:
        print("No numeric columns found in the dataset.")
        return

    print(f"Numeric columns: {num_cols}")

    for col in num_cols:
        out_html, out_png = make_histogram(df, col, nbins=args.nbins)
        print(f"Saved histogram for {col} -> {out_html}")
        interp = summary_and_interpretation(df, col)
        print(interp)
        if args.compare:
            res = compare_by_category(df, col)
            if res:
                print(f"Saved comparison histogram -> {res[0]}")


if __name__ == "__main__":
    main()
