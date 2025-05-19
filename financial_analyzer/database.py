import os
import sqlite3
from typing import Any, Iterable

DB_PATH = "data/financial.db"


def init_db(path: str = DB_PATH) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY AUTOINCREMENT, sheet TEXT, statement TEXT, data TEXT)"
    )
    conn.commit()
    return conn


def save_record(conn: sqlite3.Connection, sheet: str, statement: str, data: str) -> None:
    conn.execute(
        "INSERT INTO records (sheet, statement, data) VALUES (?, ?, ?)",
        (sheet, statement, data),
    )
    conn.commit()

