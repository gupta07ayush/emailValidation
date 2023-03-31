'''
Conditions for email validation using regex:
a-z
0-9
only one. _
only one @
. postion 2nd/3rd from last 
'''


import re

email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your Email ID: ")

if re.search(email_conditions, user_email):
    print("Right Email")
else:
    print("Wrong Email")