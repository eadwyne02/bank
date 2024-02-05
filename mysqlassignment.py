import mysql.connector as sql
mycon=sql.connect(host='127.0.0.1', user='root', passwd='', database='student_database')

mycursor=mycon.cursor()

# mycursor.execute("CREATE DATABASE student_database")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE student_table(matric_no INT(5) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(20) UNIQUE, mobileno INT(11), department VARCHAR(20), faculty VARCHAR(40) )")
mycursor.execute("ALTER TABLE student_table CHANGE (matric_no serial_no INT(5) AUTO_INCREMENT)")
# mycursor.execute("ALTER TABLE student_table")

# my= "INSERT INF  O "