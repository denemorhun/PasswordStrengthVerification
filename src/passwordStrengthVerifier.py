# Python3 code to validate a password
# author: Denem Orhun

''' Changelog (latest on top):
    # Add Phase 3
    # Add test scaffolding to cover Phase 3 and Phase 4
    # Refactor Phase 1 & 2
    # Add Phase 2 output messages
    # Add Pytests
    # Add Phase 1 initial take
    # Plan
'''

'''
PHASE 3:

Iteration 3
The tool must now take into account the type of user that a password is for. Admin users require a 
stronger password than regular users.

Passwords for Admin users must be at least 13 characters in length

Passwords for Admin users must contain a special character ('!', '@', '#', '$', '%', '^', '&', or '*')

The password requirements for regular users are unchanged

Data provided: “password123” and “normal”
Expected behavior: The password is accepted

Data provided: “password123” and “admin”
Expected behavior: The password is not accepted

Data provided: “password1234!” and “admin”
Expected behavior: The password is accepted

'''


def verifyPassword(password):

    alpha_status = True
    digit_status = True
        
    if len(password) < 8:
        print("Password is less than 8 characters")
        return False

    # refactored code to make it cleaner and expendable
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        digit_status = False

    if not any(char.isalpha() for char in password):
        print('Password should have at least one character')
        alpha_status = False

    if alpha_status is False or digit_status is False:
        return False

    return True

def print_helper( input ):
    print("Password is accepted" if input else "Password is not accepted")