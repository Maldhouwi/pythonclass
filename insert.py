import sqlite3
conn = sqlite3.connect('test.db')
print("opened database succesfully")

conn.execute("INSERT INTO STUDENTS VALUES(11,'FAITH',23,13400.00)")
conn.execute("INSERT INTO STUDENTS VALUES(12,'MARK',31,133400.00)")
conn.execute("INSERT INTO STUDENTS VALUES(13,'JANE',28,46400.00)")
conn.execute("INSERT INTO STUDENTS VALUES(14,'ALLAN',43,14400.00)")
conn.execute("INSERT INTO STUDENTS VALUES(15,'IAN',29,57400.00)")


conn.commit()
print("Records inserted succesfully")
conn.close()
