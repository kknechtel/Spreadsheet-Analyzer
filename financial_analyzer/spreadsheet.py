import pandas as pd
from typing import List, Dict
import re


def load_workbook(path: str) -> Dict[str, pd.DataFrame]:
    """Load all sheets from an Excel file into a dictionary of DataFrames."""
    xls = pd.ExcelFile(path, engine="openpyxl")
    sheets = {name: xls.parse(name) for name in xls.sheet_names}
    return sheets


def detect_statement_type(df: pd.DataFrame) -> str:
    """Naive detection of financial statement type based on keywords."""
    text = " ".join(df.columns.astype(str)).lower()
    if re.search(r"cash.?flow", text):
        return "cash_flow"
    if re.search(r"balance", text):
        return "balance_sheet"
    if re.search(r"income", text):
        return "income_statement"
    return "unknown"


def extract_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Extract numeric columns and convert currency strings."""
    numeric_df = df.copy()
    for col in numeric_df.columns:
        numeric_df[col] = (
            numeric_df[col]
            .astype(str)
            .str.replace(r"[^0-9.-]", "", regex=True)
            .replace("", pd.NA)
            .astype(float)
        )
    return numeric_df

