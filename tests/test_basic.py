import importlib
import os
import unittest

pandas_spec = importlib.util.find_spec("pandas")
openpyxl_spec = importlib.util.find_spec("openpyxl")
has_deps = pandas_spec is not None and openpyxl_spec is not None


@unittest.skipUnless(has_deps, "pandas and openpyxl are required for this test")
class SpreadsheetTest(unittest.TestCase):
    def setUp(self):
        import pandas as pd
        df = pd.DataFrame({"cash flow": [100, 200], "period": [1, 2]})
        os.makedirs("tests/test_data", exist_ok=True)
        df.to_excel("tests/test_data/sample.xlsx", index=False, sheet_name="CashFlow")

    def test_load_sample(self):
        from financial_analyzer import spreadsheet
        sheets = spreadsheet.load_workbook("tests/test_data/sample.xlsx")
        self.assertIn("CashFlow", sheets)
        df = sheets["CashFlow"]
        self.assertFalse(df.empty)


if __name__ == "__main__":
    unittest.main()
