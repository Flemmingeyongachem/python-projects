import re
def checkpass():
    username = input('Enter your password for Verification: ')
    while True:
        if not (username[0].islower() and len(username)>= 8):
            print(f"name must start with an lowercase letter")
            print('name must be longer than 8 characters.')
            checkpass()
        if (username.isdecimal() and not(re.search('[@#$%^%&*()]', username))):
            print('name cannot contain a decimal number')
            print('name must contain atleast one special character.')
            checkpass()
        if not (any(i.upper() for i in username) and any(i.isdigit() for i in username)):
            print('name must contain atleast one uppercase character.')
            print('name must contain atleast a number.')
            checkpass()
        else:
            print('very valid password')
            break
checkpass()







'''def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
import re
def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))
    or return bool(re.search( r'-?\d+',inputstring)) //to match negative numbers in a string
'''