import sqlite3
from contextlib import contextmanager


class Database:
    DB_PATH = "data/chinook.db"

    @staticmethod
    @contextmanager
    def get_connection(db_path: str = None):
        """Context manager for SQLite database connection.

        Args:
            db_path (str, optional): Path to the database file. Defaults to None.
        """
        if db_path is None:
            db_path = Database.DB_PATH
            
        conn = sqlite3.connect(db_path)
        try:
            yield conn
        finally:
            conn.close()

    @staticmethod
    @contextmanager
    def get_cursor(db_path: str = None):
        """Context manager that yields a cursor.
        
        Args:
            db_path (str, optional): Path to the database file. Defaults to None.
        """
        with Database.get_connection(db_path) as conn:
            yield conn.cursor()
