from db import cursor, conn

class MotorcycleEvent:
    TABLE_NAME = "motorcycle_events"

    def __init__(self, image_url, title, event_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.event_date = event_date

    def save(self):
        if self.id is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, title, event_date)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.title, self.event_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted motorcycle event with ID: {self.id}")

    def _update(self):
        sql = f"""
        UPDATE {self.TABLE_NAME}
        SET image_url = ?, title = ?, event_date = ?
        WHERE id = ?
        """
        cursor.execute(sql, (self.image_url, self.title, self.event_date, self.id))
        conn.commit()
        print(f"Updated motorcycle event with ID: {self.id}")

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'event_date': self.event_date,
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
    def get_by_id(cls, event_id):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        WHERE id = ?
        """
        cursor.execute(sql, (event_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return cls.row_to_instance(row)

    @classmethod
    def delete_by_id(cls, event_id):
        sql = f"""
        DELETE FROM {cls.TABLE_NAME}
        WHERE id = ?
        """
        cursor.execute(sql, (event_id,))
        conn.commit()

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        event = cls(image_url=row[1], title=row[2], event_date=row[3])
        event.id = row[0]
        return event

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
            title TEXT NOT NULL,
            event_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()

# Create the motorcycle_events table
MotorcycleEvent.create_table()

# Load the motorcycle events
motorcycle_events = [
    {
        "image_url": "https://i.ytimg.com/vi/uGIpA6puuho/sddefault.jpg",
        "title": "Dakar Rally 2024",
        "event_date": "2024-01-01"
    },
    {
        "image_url": "https://i.ytimg.com/vi/wCWvdLEfHe4/maxresdefault.jpg",
        "title": "MotoGP World Championship",
        "event_date": "2024-03-31"
    },
    {
        "image_url": "https://mediapool.bmwgroup.com/cache/P9/202302/P90495360/P90495360-munich-17th-february-2023-bmw-motorrad-motorsport-fim-superbike-world-championship-2023-media-guide-2121px.jpg",
        "title": "Superbike World Championship",
        "event_date": "2024-04-15"
    },
    {
        "image_url": "https://cdn-az.allevents.in/events5/banners/c6cfa70f5bba877d30936445d72e06bc6e6080ac703ccd3403b4756f993138ce-rimg-w1200-h917-gmir.jpg?v=1711621387",
        "title": "Motorcycle Expo 2024",
        "event_date": "2024-05-01"
    },
    {
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsiYXDgp5-308iB6BYGO7Myur-zCoNYf2U3Q&s",
        "title": "Motorcycle Grand Prix",
        "event_date": "2024-06-30"
    },
    {
        "image_url": "https://img1.wsimg.com/isteam/ip/d139d470-7f2d-4b7e-be8d-85ed125ce22e/wide%20open%20WI.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true",
        "title": "Motorcycle Stunt Show",
        "event_date": "2024-08-15"
    },
    {
        "image_url": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/moto-racing-flyer-design-template-8233486589acd329cefa2d43b534fe18_screen.jpg?ts=1694944841",
        "title": "Motorcycle Racing Festival",
        "event_date": "2024-09-30"
    },
    {
        "image_url": "https://img.freepik.com/premium-psd/motorbike-adventure-poster-template_23-2149873027.jpg",
        "title": "Motorcycle Enthusiast Gathering",
        "event_date": "2024-11-15"
    }
]

for event in motorcycle_events:
    new_event = MotorcycleEvent(
        image_url=event["image_url"],
        title=event["title"],
        event_date=event["event_date"]
    )
    new_event.save()
