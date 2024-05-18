import sqlite3

con = sqlite3.connect('myDB.db')
cursor = con.cursor()

# cursor.execute("""CREATE TABLE people
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER)
#             """)
# cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")
# bob = ("Bob", 42)
# cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", bob)
# con.commit()

cursor.execute("SELECT * FROM people")
print(cursor.fetchall())
