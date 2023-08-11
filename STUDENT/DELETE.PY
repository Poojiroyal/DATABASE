import sqlite3
conn =sqlite3.connect('test.db')
conn.execute("DELETE from STUDENT where ID=2")
conn.commit()
print("Total number of rows deleted: ",conn.total_changes)
cursor= conn.execute("SELECT id,name,dept,attendence from STUDENT")
for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("DEPT =",row[2])
    print("ATTENDENCE =",row[3])
conn.close()