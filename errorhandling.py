# # user= int(input("number:"))
# # print(user)
# colors=[
#     "red",
#     "orange",
#     "yellow",
#     "blue"
# ]
# # print(colors[10])
# # basically, we use "try"and "except" also "else" and "finally" can be used  to handle errors while programming"
# # we have the compile type error and run time error 

# # x=12
# # if x==:
# #     print(x)

# try:
#     colors["u",8]
# except IndexError:
#     print("your list doesn't have that index :-(")
# except TypeError:
#     print("list indices must be integers")
# # if you dont know the type if error that you want to handle, use
# except:
#     print("Invalid")
# # print("hello")
# else:
#     print("No error")
# finally:
#     print("with or without error I would show up")

# val1=int(input("value1:"))
# val2=int(input("value2:"))
# print(val1/val2)

# try:
#     val1=int(input("value1:"))
#     val2=int(input("value2:"))
#     print(val1/val2)
# except ValueError:
#     print("Input a number")
# except ZeroDivisionError:
#     print("your device can't be zero")
#     raise ZeroDivisionError("You are not serious")


# file handling
# with open(r"c:\Users\Adeyi Samuel\3D Objects\Desktop\Document (21).docx",mode='rb', encoding='utf-8') as myfile:
#     print(myfile.read())
# r=read only
# a= append
# w= write
# x= create



# file= open(r"C:\python class\victor.docx", 'w')
# file.write('My name is Victor')
# # print("file created")


# seperate a file with students grades and scores
# separste the files based on the grades

import os
# os gives the ability create a file, folder, delete os and lots
if os.path.exists("C:\python class\vitor.docx"):
    print("file exist")
    print("-"98)
    with open