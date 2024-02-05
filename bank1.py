import sys
def welcome():
    print("Good Morning Dear esteemed customer. Welcome to GT bank app services")
    option= input("""
        Do you want to Create an account with us?
        1. Yes
        2. No
         
""")
    x=int(0)
    if option=="1":
        print("Good that you have decided to bank with us.  Please fill the following informations")
        first_name=input("Enter your First name: ")
        last_name=input("Enter your Last name: ")
        other_name=input("Enter your other name: ")
        state_of_origin=input("Enter your State of Origin: ")
        l_g_a= input("Enter your Local Government Area: ")
        Adress= input("Enter your adress: ")
        Age= int(input("Enter your age: "))
        while True:
            b_v_n= input("Enter Your Bank Verification Number: ")
            if len(b_v_n)!=11:
                print("Incorrect Bank Verification Number: ")
            else:
                break
        while True:
            mobile_no= input("Enter Your Mobile number: ")

            if len(mobile_no)!=11:
                print("Incorrect Mobile number")
            else:
                break
        while True:
            n_i_n= input("Enter Your National Identity Number: ")
            if len(n_i_n)!=11:
                print("Incorrect National Identity Number")
            else:
                break
        while True:
            pin= input("Enter Your four digit pin: ")
            if len(pin)!=4:
                print("Unidentified pin")
            else:
                break
        if Age<16:
            print("You are underaged and not eligible to have a bank account")
            exit()
        acc_no=int(str(mobile_no)[1:])
        details= input("""
        1. View Details
        2. Exit
        """)
        if details=="1":
            print(f"""
            First name={first_name}
            Last name={last_name}
            Other name={other_name}
            Sate of Origin={state_of_origin}
            Local Government Area={l_g_a}
            Adress={Adress}
            Age={Age}
            Bank Verification Number={b_v_n}
            Mobile Number={mobile_no}
            National Identity Number={n_i_n}
            """)
            correction=input(f"""
                1. proceed
                2. Exit
                """)
            if correction=="1":
             print(f"Dear {first_name} {last_name} Good that you have decided to bank with us.")
             print(f"Your Account number is {acc_no} and your Account balance is {x}")
             deposite= input(f"""
                1. Make deposite
                2. Exit
                """)
             while True: 
                if deposite=="1":
                    fund=int(input("How much do you want to fund your account with: "))
                    x+=fund
                    print(f"Congratulations, Your account has been funded with {fund} and your balance is {x}")
                    fund_again= input(f"""
                    1. Fund account again
                    2. Other Transaction
                    3. Exit
                    """)
                    if fund_again=="1":
                        continue
                    elif fund_again=="2":
                        y=4
                        while True:
                            entry_pin=input("Enter your four digit pin: ")
                            if entry_pin==pin:
                                break
                            else:
                                y-=1
                                print(f"""Invalid Pin. You have {y} attempts left""")
                                if y==0:
                                    print("Your account has been suspended. Go to the nearest GT bank branch")
                                    exit()
                                try_again=input(f"""
                                1. Try again
                                2. Exit
                                """)
                                if try_again=="1":
                                    pass
                                elif try_again=="2":
                                    sys.exit
                        while True: 
                            transaction= input(f"""
                            1. Make Tranfer
                            2. Fund account
                            3. Account balance inquiry
                            4. Buy Airtime 
                            5. Buy data
                            6. Exit
                            : """)
                            if transaction=="1":
                                while True:
                                    transfer_number= input("Enter recipient account number: ")
                                    if len(transfer_number)!=10:
                                        print("Invalid account number")
                                    else:
                                        break
                                transfer_bank= input("Enter recipient bank name: ")
                                while True: 
                                    transfer_amount= int(input("Enter amount: "))
                                    while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                    if transfer_amount>x:
                                        insufficient_amount=("""Insufficient amount
                                        1. Try again
                                        2. Exit
                                        """)
                                        if insufficient_amount=="1":
                                            continue
                                        elif insufficient_amount=="2":
                                            sys.exit
                                    else:
                                        break
                                print(f"You have Successfully transferred {transfer_amount} to {transfer_number}")
                                x-=transfer_amount
                                print(f" Your account has been debitted with {transfer_amount}. Your balance is {x} ")
                            elif transaction=="2":
                                fund=int(input("How much do you want to fund your account with: "))
                                x+=fund
                                print(f"Congratulations, Your account has been funded with {fund} and your balance is {x}")
                            elif transaction=="3":
                                while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                print(f"Your account balance is {x}")
                            elif transaction=="4":
                                while True:
                                    airtime= int(input("Enter phone number: "))
                                    if len(airtime)!=10:
                                        print("Invalid Phone number")
                                    else:
                                        break
                                airtime_amount= int(input("Enter airtime amount:"))
                                while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                if airtime_amount>x:
                                    print("Insufficient Balance")
                                else:
                                    print(f"Airtime Successful")
                                x-=airtime_amount
                                print(f"Your account has been debitted with {airtime_amount}. Your remaining balance is {x}")
                            elif transaction=="5":
                                data= input("""
                                purchase
                                1. 500mb for 130#
                                2. 1gb for 260#
                                3. 2gb for 520#
                                4. 5gb for 1300#
                                5. Exit
                                """)
                                if data=="1":
                                    while True:
                                        airtime= int(input("Enter phone number: "))
                                        if len(airtime)!=10:
                                            print("Invalid Phone number")
                                        else:
                                            break
                                    while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                    x-=130
                                    print("Data Purchase successful")
                                    print(f"Your account has been debitted with 130#. Your remaining balance is {x}#")
                                elif data=="2":
                                    while True:
                                        airtime= int(input("Enter phone number: "))
                                        if len(airtime)!=10:
                                            print("Invalid Phone number")
                                        else:
                                            break
                                    while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                    x-=260
                                    print("Data Purchase successful")
                                    print(f"Your account has been debitted with 260#. Your remaining balance is {x}#")
                                elif data=="3":
                                    while True:
                                        airtime= int(input("Enter phone number: "))
                                        if len(airtime)!=10:
                                            print("Invalid Phone number")
                                        else:
                                            break
                                    while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                    x-=520
                                    print("Data Purchase successful")
                                    print(f"Your account has been debitted with 520#. Your remaining balance is {x}#")
                                elif data=="4":
                                    while True:
                                        airtime= int(input("Enter phone number: "))
                                        if len(airtime)!=10:
                                            print("Invalid Phone number")
                                        else:
                                            break
                                    while True: 
                                        pass_pin= input("Enter  your four digit pin:")
                                        if pass_pin==pin:
                                            break
                                        else:
                                            y-=1
                                            print(f"""Invalid Pin. You have {y} attempts left""")
                                            if y==0:
                                                print("Your account has been suspended. Go to the nearest GT bank branch")
                                                exit()
                                    x-=1300
                                    print("Data Purchase successful")
                                    print(f"Your account has been debitted with 1300#. Your remaining balance is {x}#")
                                elif data=="5":
                                    sys.exit
                    elif fund_again=="3":
                        sys.exit
                    else:
                        ("Invalid Input")
                else:
                    sys.exit
        elif details=="2":
            sys.exit
           
            
    elif option=="2":
        sys.exit
    else:
        print("Invalid Input")
    # else:
    #     welcome()
welcome()