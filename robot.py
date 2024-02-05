status=input ("Who are you? \n a student, staff or visitor: ")
if status.capitalize()=="Student":
    print("""
    1. I have paid my fees in full
    2. I have paid my fees in part
    3. haven't paid my fees at all
    """)
    fees=input(" Enter your fee status: ")
    if fees=="1":
        print("Hi today, kindly move to your class")
    elif fees=="2":
        print("Please do well to balance up befroe this week runs to an end else you won't ba permittted to take classes from next week")
    elif fees=="3":
        print("Not permitted in.. Do pay your fees")
    else:
        print("Go back")
elif status.capitalize()== "Staff":
    print("Your Welcome today")
elif status.capitalize()== "Visitor":
    print("You are welcome to SQI college of ICT. Kindly visit our front desk for more informatiom")
else:
    print("You are not welcomed")
