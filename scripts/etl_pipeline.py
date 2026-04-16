from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Template ETL pipeline: raw -> cleaned -> Tableau-ready exports"
    )
    p.add_argument(
        "--raw",
        required=True,
        help="Path to raw CSV (e.g. data/raw/dataset.csv)",
    )
    p.add_argument(
        "--outdir",
        default="data/processed",
        help="Output directory for processed files (default: data/processed)",
    )
    p.add_argument(
        "--encoding",
        default=None,
        help="Optional CSV encoding override (e.g. utf-8, latin-1)",
    )
    return p.parse_args()


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Project-specific cleaning belongs here.
    Keep it deterministic and testable; notebooks can explore, this script should produce final artifacts.
    """
    df = standardize_columns(df)
    df = df.drop_duplicates()
    return df


def build_tableau_exports(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """
    Return a mapping of filename -> dataframe for Tableau consumption.
    Replace with your project grain/aggregations.
    """
    return {
        "tableau_fact.csv": df,
    }


def main() -> int:
    args = _parse_args()
    raw_path = Path(args.raw)
    out_dir = Path(args.outdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df_raw = pd.read_csv(raw_path, encoding=args.encoding)
    df_clean = clean(df_raw)

    cleaned_path = out_dir / "cleaned.csv"
    df_clean.to_csv(cleaned_path, index=False)

    exports = build_tableau_exports(df_clean)
    for name, df in exports.items():
        df.to_csv(out_dir / name, index=False)

    print(f"Wrote: {cleaned_path}")
    for name in exports.keys():
        print(f"Wrote: {out_dir / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
