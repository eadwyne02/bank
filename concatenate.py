# methods of concatenation on python
# using '+ orperator'
# first_name = input("First Name : ")
# greeting = ("Hello ")
# result= greeting + first_name
# print (result)


# using the '%' oprator
# institution = input("Name of ypur institution : ")
# location = input("The location of your institution : ")
# result= "%s %s"%(institution , location)
# print (result)


# using join() method
# Title = input("Enter your title: ")
# name = input("Enter your name: ")
# result= " ". join([Title, name])
# print (result)


# using format() method
# lga= input("Enter your Local Gpvernment Area : ")
# state= input("Enter your state of origin : ")
# result= "{} {}". format(lga , state)
# print(result)


# using the f-string
# day=input("Enter the day of the week : ")
# month= input("enter the month of the year: ")
# result = f'{day} {month}'
# print(result)


# Greeting = ("Hello world")
# first_name= input("Enter your first name : ")
# last_name= input("Enter your last name : ")
# # result1 =  first_name +  last_name
# institution= input("Enter your college name : ")
# location= input("Enter location of your college : ")
# # result2="%s %s"%(institution , location)
# lga= input("Enter the local government area of your college : ")
# state= input("Enter the state your institution is located : ")
# # result3 = " ". join([lga, state])
# course_offering= input("Enter the course you are offering : ")
# Department= input("Enter the department of your course : ")
# # result4= "{} {}". format(course_offering , Department)
# title= input("Enter the title of your tutor : ")
# tutor= input("Enter the name of your tutor : ")
# # result5= f'{title} {tutor}'
# # note, when using the f-string, you dont need comma just need a quali bracket for your variables
# print(f" {Greeting} I am {first_name} {last_name}. I am a student of {institution} {location} {lga} {state}. I am offering {course_offering} from {Department}. The name of my tutor is {title} {tutor}" ) 
student_record= [
    ("Noah", 60, "B"),
    ("Muazeem", 72, "A"),
    ("Tikristi", 85, "A"),
    ("coded", 60, "B"),
    ("fulfilment", 70, "A")
]
for score in student_record:
    print(sum(score))