import pg8000

conn = pg8000.connect(user="postgres", password="C.P.Snow")
cursor = conn.cursor()
cursor.execute("CREATE TEMPORARY TABLE book (id SERIAL, title TEXT)")
cursor.execute("INSERT INTO book (title) VALUES (%s), (%s) RETURNING id, title", ("Ender's Game", "Speaker for the Dead"))
results = cursor.fetchall()

for row in results:
    id, title = row
    print("id = %s, title = %s" % (id, title))

conn.commit()
