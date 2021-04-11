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

# refactored code to include a class for standard user and admin user
# User class that has verify password method
class User():

    def __init__(self):
        self.CHAR_LIMIT = 8

    def verify_password(self, password):

        alpha_status = True
        digit_status = True
        
        if len(password) < self.CHAR_LIMIT:
            print(f"Password is less than {self.CHAR_LIMIT} characters")
            return False

        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            digit_status = False

        if not any(char.isalpha() for char in password):
            print('Password should have at least one character')
            alpha_status = False

        if alpha_status is False or digit_status is False:
            return False

        return True

    def _print_helper(self, input):
        print("Password is accepted" if input else "Password is not accepted")

class Admin(User):

    def __init__(self):
        self.CHAR_LIMIT = 13
        self.special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']

    def verify_admin_password(self, password):

        basic_status = self.verify_password(password)
        print("Basic Status", basic_status)
        special_char_status = True

        if basic_status is False:
            return False

        if not any(char in self.special_chars for char in password):
            print('Password should have at least one special character.')
            print("Refer to this list: '!', '@', '#', '$', '%', '^', '&' '*'")
            special_char_status = False

        if special_char_status is False or basic_status is False:
            print('Returning false')
            return False
        else:
            print('Returning true')
            return True

    

# user1  = User()
# user1._print_helper(user1.verify_password('111111111111'))
# user1._print_helper(user1.verify_password('8888dddd'))
# user1._print_helper(user1.verify_password('        '))
# user1._print_helper(user1.verify_password('uiurerererare'))
# user1._print_helper(user1.verify_password('ADERE3232425'))
# user1._print_helper(user1.verify_password('@#$@#$#@$@$$@$@'))
# user1._print_helper(user1.verify_password('@#$@$@ADAFDAF23423424'))
# user1._print_helper(user1.verify_password('111111111111'))


admin1 = Admin()
admin1._print_helper(admin1.verify_admin_password('111'))
admin1._print_helper(admin1.verify_admin_password('111111111@11111111'))
admin1._print_helper(admin1.verify_admin_password('@1111dddddddddddd'))

admin1._print_helper(admin1.verify_admin_password('ABDC23423443dadafdad'))

print(admin1.verify_admin_password('ABDC23423443dadafdad'))