import sqlite3

class MotorcycleOffer:
    TABLE_NAME = "motorcycle_offers"

    def __init__(self, image_url, title, category, initial_price, current_price, rating, release_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.category = category
        self.initial_price = initial_price
        self.current_price = current_price
        self.rating = rating
        self.release_date = release_date

    def save(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, title, category, initial_price, current_price, rating, release_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.title, self.category, self.initial_price, self.current_price, self.rating, self.release_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted motorcycle offer with ID: {self.id}")
        conn.close()

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql_drop = f"""
        DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql_drop)
        conn.commit()

        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            initial_price TEXT NOT NULL,
            current_price TEXT NOT NULL,
            rating TEXT NOT NULL,
            release_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = f"SELECT * FROM {cls.TABLE_NAME}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        motorcycle_offers = []
        for row in rows:
            motorcycle_offer = MotorcycleOffer(
                image_url=row[1],
                title=row[2],
                category=row[3],
                initial_price=row[4],
                current_price=row[5],
                rating=row[6],
                release_date=row[7]
            )
            motorcycle_offer.id = row[0]
            motorcycle_offers.append(motorcycle_offer)
        conn.close()
        return motorcycle_offers

    def to_dict(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "title": self.title,
            "category": self.category,
            "initial_price": self.initial_price,
            "current_price": self.current_price,
            "rating": self.rating,
            "release_date": self.release_date
        }

# Create the table if it doesn't exist
MotorcycleOffer.create_table()

motorcycle_offers_data = [
    {
        "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/octane/M225VSEIKFGPJBL3ZWQ44XIRKI.jpg",
        "title": "Ducati Monster 797",
        "category": "Cruiser",
        "initial_price": "Ksh 1,200,000",
        "current_price": "Ksh 900,000",
        "rating": "5",
        "release_date": "2016-05-19",
        "discount": "25%"
    },
    {
        "image_url": "https://www.motorbeam.com/wp-content/uploads/2013-Yamaha-FZ6R-Front-White.jpg",
        "title": "Yamaha FZ6R",
        "category": "Sport",
        "initial_price": "Ksh 1,100,000",
        "current_price": "Ksh 850,000",
        "rating": "5",
        "release_date": "2018-01-26",
        "discount": "23%"
    },
    {
        "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/octane/S6UJXJWJLZC5RMX7CYJZZ6OXKQ.jpg",
        "title": "Honda CBR500R",
        "category": "Sport",
        "initial_price": "Ksh 1,300,000",
        "current_price": "Ksh 1,000,000",
        "rating": "5",
        "release_date": "2017-03-03",
        "discount": "23%"
    },
    {
        "image_url": "https://www.colchesterkawasaki.co.uk/upload/images/2023%20kawasaki/NINJA%20650/2023%20Ninja%20650%20GN.png",
        "title": "Kawasaki Ninja 650",
        "category": "Sport",
        "initial_price": "Ksh 1,200,000",
        "current_price": "Ksh 900,000",
        "rating": "5",
        "release_date": "2017-10-27",
        "discount": "25%"
    },
    {
        "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/octane/GZUQ6YFSEJFELJDW6HCZB2MGYE.jpg",
        "title": "Suzuki GSX250R",
        "category": "Sport",
        "initial_price": "Ksh 1,000,000",
        "current_price": "Ksh 750,000",
        "rating": "4",
        "release_date": "2017-07-21",
        "discount": "25%"
    },
    {
        "image_url": "https://kickstart.bikeexif.com/wp-content/uploads/2014/12/custom-harley-davidson-street-1.jpg",
        "title": "Harley-Davidson Street 750",
        "category": "Cruiser",
        "initial_price": "Ksh 1,400,000",
        "current_price": "Ksh 1,100,000",
        "rating": "5",
        "release_date": "2016-09-15",
        "discount": "21%"
    },
    {
        "image_url": "https://bd.gaadicdn.com/processedimages/triumph/triumph-street-triple/494X300/triumph-street-triple64a7fb92db5f2.jpg",
        "title": "Triumph Street Triple",
        "category": "Sport",
        "initial_price": "Ksh 1,500,000",
        "current_price": "Ksh 1,200,000",
        "rating": "5",
        "release_date": "2020-03-20",
        "discount": "20%"
    },
    {
        "image_url": "https://www.wunderlich.de/media/7e/f7/0b/1670580273/F750GS_Nachher.jpg",
        "title": "BMW F 750 GS",
        "category": "Adventure",
        "initial_price": "Ksh 1,800,000",
        "current_price": "Ksh 1,500,000",
        "rating": "5",
        "release_date": "2019-07-26",
        "discount": "17%"
    },
]

# Insert each motorcycle offer into the database
for motorcycle_offer_data in motorcycle_offers_data:
    motorcycle_offer = MotorcycleOffer(
        image_url=motorcycle_offer_data["image_url"],
        title=motorcycle_offer_data["title"],
        category=motorcycle_offer_data["category"],
        initial_price=motorcycle_offer_data["initial_price"],
        current_price=motorcycle_offer_data["current_price"],
        rating=motorcycle_offer_data["rating"],
        release_date=motorcycle_offer_data["release_date"]
    )
    motorcycle_offer.save()
