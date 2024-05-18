import sqlite3

connection = sqlite3.connect("itstepDB.sl3", 5)
cur = connection.cursor()

print(connection)
print(cur)

# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kost');")

student = 'kopo'
# cur.execute("INSERT INTO first_table (name) VALUES ('kopo');")

cur.execute("SELECT rowid, name FROM first_table;")

connection.commit()
res = cur.fetchall()
print(res)

connection.close()
