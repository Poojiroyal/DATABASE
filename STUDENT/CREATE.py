import sqlite3
conn = sqlite3.connect('test.db')
print("Opened datebase successfuly")
conn.execute('''CREATE TABLE STUDENT
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             DEPT TEXT NOT NULL,
             ATTENDENCE REAL)''')
print("Table crreated successfully")
conn.close()