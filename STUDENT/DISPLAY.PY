import sqlite3
conn =sqlite3.connect('test.db')
result=conn.execute("SELECT id,name,dept,attendence from STUDENT")
print(result.fetchall())
print("Operation done successfully")
conn.close()