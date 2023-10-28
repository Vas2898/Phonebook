import sqlite3

con = sqlite3.connect('phonebook.db')
cur = con.cursor()
cur.execute("drop table if exists phonebook")
cur.execute("""
            CREATE TABLE PHONEBOOK
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NAME VARCHAR(25) NOT NULL,
            NUMBER INTEGER UNIQUE NOT NULL,
            LOCATION TEXT NOT NULL
            )
            """)
con.commit()
print('table created')
con.close()
