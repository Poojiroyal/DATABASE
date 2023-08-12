import sqlite3
conn =sqlite3.connect('test.db')
result=conn.execute("SELECT * FROM STUDENT")
print(result.fetchall())
print("Operation done successfully")
conn.close()