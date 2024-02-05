import sys
import mysql.connector as sql
import random
import datetime as dt
# mycon=sql.connect(host='127.0.0.1', user='root', passwd='')
mycon=sql.connect(host='127.0.0.1', user='root', passwd='', database='bank1_database')
mycursor=mycon.cursor()
# mycursor.execute("CREATE DATABASE bank1_database")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE customer_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, firstName VARCHAR(20), surName VARCHAR(20), lastName VARCHAR(20), mobileNo INT(11) UNIQUE, dayOfBirth INT(2), monthOfBirth VARCHAR(10), yearOfBrith INT(4), email VARCHAR(20) UNIQUE, adress VARCHAR(70), stateOfOrigin VARCHAR(20), pin INT(4), accountNo INT(11), accountBalance INT(20) )")
# mycursor.execute("ALTER TABLE customer_table ADD ")
# mycursor.execute("ALTER TABLE customer_table MODIFY COLUMN pin INT(7)")



# mycursor.close()
# mycon.close()


x=int(0)
pin=None
user_account_number=None
account_number= None
def check_account_number(accountNo):
    query = f"SELECT * FROM customer_table WHERE accountNo = %s"

    mycursor.execute(query, (accountNo,))
    result = mycursor.fetchone()  

    if result:
        pass
    else:
        print(f"The account number {accountNo} does not exist.")
        welcome()
def check_pin(accountNo, pin):
    query1 = "SELECT * FROM customer_table WHERE accountNo= %s AND pin = %s"
    
    mycursor.execute(query1, (accountNo, pin))
    result = mycursor.fetchone()
    if result:
        pass
    else:
        print(f"Invalid PIN for account {accountNo}.")
        welcome() 
def funds():
    global x, user_account_number
    fund = int(input("Amount in naira: "))
    
    mycursor.execute("UPDATE customer_table SET accountBalance = accountBalance + %s WHERE accountNo = %s", (fund, user_account_number))
    mycon.commit()

    mycursor.execute("SELECT accountBalance FROM customer_table WHERE accountNo = %s", (user_account_number,))
    result = mycursor.fetchone()
    if result:
        x = result[0]
        print(f"Congratulations, your account has been funded with #{fund}. Your total account balance is #{x}")
    else:
        print("Error fetching updated account balance from the database.")

    print("""
        1. Fund your account again
        2. Perform other transactions
    """)
    
    fund_again = input(": ")
    if fund_again == "1":
        funds()
    elif fund_again == "2":
        transaction()
def info():
    global pin
    global account_number
    print("Good that you have decided to bank with us")
    surName=input("Enter your surname: ")
    firstName=input("Enter your firstame: ")
    lastName=input("Enter your lastname: ")
    mobileNo=input("Enter your mobile number +234: ")
    dayOfBirth= input("Enter your day of birth: ")
    monthOfBirth=input("Emter your month of birth:")
    yearOfBrith=input("Enter your year of birth:")
    email=input("Enter your Email adress:")
    adress= input("Enter your residence adress: ")
    stateOfOrigin= input("Enter your state of Origin:")
    pin= input("Enter your four digit pin: ")
    acc_number=''.join(str(random.randint(0,9)) for _ in range(9))
    account_number="0"+acc_number   
    mycursor.execute("INSERT INTO customer_table(surName, firstName, lastName, mobileNo, dayOfBirth, monthOfBirth, yearOfBrith, email, adress, stateOfOrigin, pin, accountNo, accountBalance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(surName,firstName, lastName, mobileNo, dayOfBirth, monthOfBirth, yearOfBrith, email, adress, stateOfOrigin, pin, account_number, x))
    mycon.commit()
    
    print(f""""Congratulations dear {firstName} {lastName} 
        your account number is {account_number}
        and your balance is #{x} Fund your account now""")
    print("""
        Do you want to fund your account now?
        1. Yes
        2. No
        """)
        
    acct=input(":")
    if acct=="1":
            funds()
    elif acct=="2":
            transaction()
def transaction():
    global x, user_account_number
    print("""
    1. Make Tranfer
    2. Fund account
    3. Account balance inquiry
    4. Buy Airtime 
    5. Buy data
    6. Exit
    """)
    tim= dt.datetime.now()
    opt=input(": ")
    if opt=="1":
        acct_no=(input("Enter recepient account number: "))
        amount=int(input("How much do you want to tramsfer: "))
        user_pin = input("Enter your PIN: ")
        check_pin(user_account_number, user_pin)
        mycursor.execute("SELECT accountBalance FROM customer_table WHERE accountNo = %s", (user_account_number,))
        sender_balance = mycursor.fetchone()[0]
        if amount <= sender_balance:
            mycursor.execute("UPDATE customer_table SET accountBalance = accountBalance - %s WHERE accountNo = %s", (amount, user_account_number))
            mycursor.execute("UPDATE customer_table SET accountBalance = accountBalance + %s WHERE accountNo = %s", (amount, acct_no))
            mycon.commit()    
            x-= amount
            print("Transfer Successful")
            x-=amount
            print(f"Dear customer, you have succefully trasfered {amount} to {acct_no}. Your balance is {x}")
                
        print(f"""
        1. Back
        2. Exit.
        """)
        back= input(":")
        if back=="1":
            transaction()
        elif back=="2":
            sys.exit
    elif opt =="2":
        funds()
    elif opt=="3":
        mycursor.execute("SELECT accountBalance FROM customer_table WHERE accountNo = %s", (user_account_number,))
        result = mycursor.fetchone()

        if result:
            x = result[0]
            print(f"Your account balance as at {tim} is #{x}")
        else:
            print("Error fetching account balance from the database.")
        transaction()
    elif opt=="4":
        airtime=int(input("How much airtime do you want to purchase:"))
        airtime_no=int(input("Enter mobile number:"))
        send_balance = mycursor.fetchone()
        if airtime <= send_balance:
            mycursor.execute("UPDATE customer_table SET accountBalance = accountBalance - %s WHERE accountNo = %s", (airtime, user_account_number))
            mycursor.execute("UPDATE customer_table SET accountBalance = accountBalance + %s WHERE accountNo = %s", (airtime, acct_no))
            mycon.commit()    
        x-=airtime
        print(f"Dear customer, you have successfully purchased airtime worth {airtime}# for {airtime_no}. your balance is {x}")
        transaction()
def welcome():
    global x, user_account_number
    print("""
    Welcome to GT bank
    1. Open a GT bank account
    2. Already have an account
    3. Exit
    """)
    account = input("Enter your option: ")
    
    if account == "1":
        info()  
    elif account == "2":
        user_account_number = input("Enter the account number: ")
        check_account_number(user_account_number)
        user_pin = input("Enter your PIN: ")
        check_pin(user_account_number, user_pin)
        transaction()
    elif account == "3":
        sys.exit()  # Corrected sys.exit()
    else:
        welcome()

# Call the welcome function to start the program
welcome()

def password():
    y=int(4)
    pw=int(input("Enter your 4 digit pin:"))
    if pw==pin:
        pass
    else:
        y-=1
        print(f"Wrong pin. You have {y} attempts left")
        if y==0:
            print("Too many wrong attempts, you account has been locked. Kindly visit our nearest GT branch")


