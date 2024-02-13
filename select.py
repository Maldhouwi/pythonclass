# TO SEE THE CONTENT OF THE TABLE
import sqlite3

conn = sqlite3.connect('test.db')
print("opened database succesfully")

cursor = conn.execute("SELECT ID,NAME,AGE,SALARY FROM STUDENTS")

for row in cursor:
    print("ID",row[0])
    print("NAME",row[1])
    print("AGE",row[2])
    print("SALARY",row[3])

print("Records found")
conn.close()