# models/catalogue.py

from db import cursor

class Model:
    TABLE_NAME = 'models'

    def __init__(self, name):
        self.id = None
        self.name = name

    def save(self):
        cursor.execute(f"SELECT id FROM {self.TABLE_NAME} WHERE name = ?", (self.name,))
        result = cursor.fetchone()
        if result:
            print(f"{self.name} already exists with id {result[0]}")
        else:
            sql = f"INSERT INTO {self.TABLE_NAME} (name) VALUES (?)"
            cursor.execute(sql, (self.name,))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"{self.name} saved")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def find_all(cls):
        try:
            sql = f"SELECT * FROM {cls.TABLE_NAME}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            models = [cls.row_to_instance(row).to_dict() for row in rows]
            print(f"Fetched {len(models)} models from database")
            return models
        except Exception as e:
            print(f"Error fetching models: {e}")
            return []

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None

        model = cls(row[1])
        model.id = row[0]

        return model

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"Models table created")
