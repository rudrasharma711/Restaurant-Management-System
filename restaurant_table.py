import sqlite3
con = sqlite3.connect('restaurant.db')
cur = con.cursor()

cur.execute('''CREATE TABLE restaurant(
               name text,
               email text,
               DOB text,
               service_rating char(1),
               food_rating char(1))''')
con.commit()
con.close()
