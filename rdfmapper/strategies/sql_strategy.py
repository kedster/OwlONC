
import sqlite3
from strategies.base import DataInputStrategy

class SQLStrategy(DataInputStrategy):
    def load_data(self, filepath):
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM some_table")
        columns = [description[0] for description in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return data
