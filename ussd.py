ussd= input("Input your USSD code: ")
if ussd != "*777#":
    print("Invalid USSD code...")
else:
    print("""
    1. Data
    2. Borrow Credit or Data
    3. Buy Recharge
    4. My Tariff plan
    """)
user= input("your option: ")
if user =="1":
    print("""
    1. Buy Data Plan
    2. Match day offer
    3. Betting agent plan
    4. Showmax data plan
    """)
elif user =="2":
    print("""
    you have a credit limit 0f 1000. Service fee includes VAT
    1. Borrow #50
    2. Borrow #100
    3. Borrow #200
    4. Borrow Data
    """)
elif user =="3":
    print("""
    welcome to Glo e-service
    please select an option
    1. Airtime
    2. Data
    9. Back
    0. Exit
    """)
elif user =="4":
    print("""
    Enjoy 700% bonus to call all network + FREE Data on every recharge
    1. Migrate Now
    2. Back
    3. Exit
    """)
else:
    print("Invalid option")