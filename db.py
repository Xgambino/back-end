import sqlite3

conn = sqlite3.connect('motorcycles.db', check_same_thread = False )

cursor = conn.cursor()