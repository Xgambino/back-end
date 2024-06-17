from db import cursor, conn

class Catalogue:
    TABLE_NAME = "motorcycles"
    
    def __init__(self, image_url, brand, model, category, price, rating, release_date):
        self.id = None
        self.image_url = image_url
        self.brand = brand
        self.model = model
        self.category = category
        self.price = price
        self.rating = rating
        self.release_date = release_date

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, brand, model, category, price, rating, release_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.brand, self.model, self.category, self.price, self.rating, self.release_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted motorcycle with ID: {self.id}")
        print(f"{self.brand}, {self.model}, {self.category}, {self.price}, {self.rating}, {self.release_date}, {self.image_url}")

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'brand': self.brand,
            'model': self.model,
            'category': self.category,
            'price': self.price,
            'rating': self.rating,
            'release_date': self.release_date
        }

    @classmethod
    def get_all(cls):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.row_to_instance(row) for row in rows]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        motorcycle = cls(image_url=row[1], brand=row[2], model=row[3], category=row[4], price=row[5], rating=row[6], release_date=row[7])
        motorcycle.id = row[0]
        return motorcycle

    @classmethod
    def create_table(cls):
        sql_drop = f"""
        DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql_drop)
        conn.commit()

        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            category TEXT NOT NULL,
            price TEXT NOT NULL,
            rating TEXT NOT NULL,
            release_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()
        
    @classmethod
    def get_by_id(cls, motorcycle_id):
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?"
        cursor.execute(sql, (motorcycle_id,))
        row = cursor.fetchone()
        return cls.row_to_instance(row)

# Call create_table to ensure the table exists
Catalogue.create_table()

motorcycle_data = [
    {
        "img": "https://example.com/motorcycle1.jpg",
        "brand": "Yamaha",
        "model": "YZF-R1",
        "category": "Sport",
        "price": "Ksh 1,500,000",
        "rating": "5",
        "releaseDate": "Release Date: 2022-06-15"
    },
    {
        "img": "https://example.com/motorcycle2.jpg",
        "brand": "Honda",
        "model": "CBR600RR",
        "category": "Sport",
        "price": "Ksh 1,200,000",
        "rating": "4.5",
        "releaseDate": "Release Date: 2021-05-10"
    },
    {
        "img": "https://example.com/motorcycle3.jpg",
        "brand": "Ducati",
        "model": "Panigale V4",
        "category": "Sport",
        "price": "Ksh 2,000,000",
        "rating": "5",
        "releaseDate": "Release Date: 2023-03-20"
    },
    {
        "img": "https://example.com/motorcycle4.jpg",
        "brand": "Harley-Davidson",
        "model": "Street Glide",
        "category": "Cruiser",
        "price": "Ksh 2,500,000",
        "rating": "4.5",
        "releaseDate": "Release Date: 2020-09-25"
    },
    {
        "img": "https://example.com/motorcycle5.jpg",
        "brand": "Kawasaki",
        "model": "Ninja H2",
        "category": "Sport",
        "price": "Ksh 2,200,000",
        "rating": "5",
        "releaseDate": "Release Date: 2021-12-15"
    }
]

for card in motorcycle_data:
    motorcycle = Catalogue(
        image_url=card["img"],
        brand=card["brand"],
        model=card["model"],
        category=card["category"],
        price=card["price"],
        rating=card["rating"],
        release_date=card["releaseDate"]
    )
    motorcycle.save()