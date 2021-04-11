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

# User class with verify password method
class User():
    def __init__(self):
        self.CHAR_LIMIT = 8

    def _verify_password(self, password):

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

    def is_pwd_valid(self, input):
        print("Password is accepted" if input else "Password is not accepted")

# Admin Class extends user and 
class Admin(User):

    def __init__(self):
        self.CHAR_LIMIT = 13
        self.special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']

    def _verify_admin_password(self, password):

        basic_status = self._verify_password(password)
        print("Basic Status", basic_status)
        special_char_status = True

        if basic_status is False:
            return False

        if not any(char in self.special_chars for char in password):
            print('Password should have at least one special character.')
            print("Refer to this list: '!', '@', '#', '$', '%', '^', '&' '*'")
            special_char_status = False

        if special_char_status is False or basic_status is False:
            return False
        else:
            print('Returning true')
            return True