# regex regular expression
# for pattern matching
import re

# def check_for_email(email):
#     pattern= r'^\w+@\w+\.\w+$'
#     # ^ to assert the start of a sting
#     # \. matches the literal "." symbol.
#     # w stands for string
#     # w+$ means must end with one or more string
#     matches= re.match(pattern, email)
#     # print(matches)
#     if matches:
#         print("valid email")
#     else:
#         print("invali email")

# inp= input("Email:")
# check_for_email(inp)


# pattern= r'[a-z]'
# string='abc def'
# matche= re.match(pattern, string)
# print(matche)
# if matche:
#     print("There is match")
# else:
#     print("there is no matchs")

# .search
# pattern=r'abc'
# string='qabc abc abc'
# match = re.search(pattern, string)
# print(match)
# if match:
#     print('Match found')
# else:
#     print("match not found")
# li=[]
# x= range(10)
# for num in x:
#     li.append(num)

# x= list(range(10)*2)
# print(x)
x=[num*2 for num in range(10)]
print(x)