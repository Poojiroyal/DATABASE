import sqlite3
conn = sqlite3.connect('test.db')
conn.execute("UPDATE STUDENT set ATTENDENCE = 95 where ID=1")
conn.commit()
print("Total number of rows update: ",conn.total_changes)
cursor=conn.execute("SELECT id,name,dept,attendence from STUDENT")
for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("DEPT =",row[2])
    print("ATTENDENCE =",row[3])
print("Operation done successfully")
conn.close()