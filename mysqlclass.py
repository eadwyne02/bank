import mysql.connector as sql
# mycon=sql.connect(host='127.0.0.1', user='root', passwd='')
mycon=sql.connect(host='127.0.0.1', user='root', passwd='', database='bank_database')

mycursor=mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)



# mycusor.execute("SHOW DATABASE")
# for db in mycusor:
#     print(db)

# mycursor.execute("CREATE DATABASE bank_database")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE customer_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), 
# email VARCHAR(20) UNIQUE, username VARCHAR(20) UNIQUE, password VARCHAR(20) )")


# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)
# mycursor.execute("ALTER TABLE customer_table CHANGE id ctm_id INT(4) AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customer_table ADD (account_no VARCHAR(15) UNIQUE, account_bal FLOAT(15))")
# mycursor.execute("ALTER TABLE customer_table ADD account_bal FLOAT(15)")

# insert values into data base

# mycursor.execute("INSERT INTO customer_table (fullname, email, username, password, account_no, account_bal) VALUES('Ajayi Badmus', 'ajayi@gmail.com', 'ajayi', '1234', '1234567890', 1000)")
# mycon.commit()

myquerry= "INSERT INTO customer_table(fullname, email, username, password, account_no, account_bal) VALUES(%s,%s,%s,%s,%s,%s)"
val1=('Timi Adesola', 'Owolake', 'Timi', '1234', '2079430102', 75000.43)
mycursor.execute(myquerry,val1)
mycon.commit()
print(mycursor.rowcount, "record inserted successfully")