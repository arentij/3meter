import pg8000

cursor.execute("SELECT extract(millennium from now())")
cursor.fetchone()