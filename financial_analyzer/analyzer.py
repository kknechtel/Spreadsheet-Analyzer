from typing import Dict
import json

import pandas as pd

from . import spreadsheet
from . import llm_service
from . import database


class Analyzer:
    def __init__(self, db_path: str = database.DB_PATH):
        self.conn = database.init_db(db_path)

    def process_file(self, path: str) -> Dict[str, pd.DataFrame]:
        sheets = spreadsheet.load_workbook(path)
        for name, df in sheets.items():
            statement = spreadsheet.detect_statement_type(df)
            numeric_df = spreadsheet.extract_numeric(df)
            database.save_record(
                self.conn,
                sheet=name,
                statement=statement,
                data=numeric_df.to_json(),
            )
        return sheets

    def analyze_with_llm(self, prompt: str) -> str:
        return llm_service.call_openai(prompt)

