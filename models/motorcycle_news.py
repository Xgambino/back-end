from db import cursor, conn

class Model:
    TABLE_NAME = 'models'
    def __init__(self, name) -> None:
        self.id = None
        self.name = name
    
    def save(self):
        # Check if the name already exists
        cursor.execute(f"SELECT id FROM {self.TABLE_NAME} WHERE name = ?", (self.name,))
        result = cursor.fetchone()
        if result:
            print(f"{self.name} already exists with id {result[0]}")
        else:
            sql = f"""
                INSERT INTO {self.TABLE_NAME} (name)
                VALUES (?)
            """
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
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        """
        
        rows = cursor.execute(sql).fetchall()

        return [cls.row_to_instance(row).to_dict() for row in rows]

    @classmethod
    def row_to_instance(cls, row):
        if row == None:
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

# def main():
#     Model.create_table()

#     models = ["Kawasaki", "Yamaha", "BMW", "Jincheng", "Taro"]

#     for model_name in models:
#         model = Model(model_name)
#         model.save()

#     all_models = Model.find_all()
#     print("All models in the database:")
#     for model in all_models:
#         print(model)

# if __name__ == "__main__":
#     main()
