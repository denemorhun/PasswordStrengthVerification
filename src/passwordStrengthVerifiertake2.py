# Python3 code to validate a password

# ITERATION 1 COMMIT
  
''' Iteration 1
The tool should verify if a password meets the requirements for a strong password
• The password must be at least 8 characters in length 
-- what about upper limit?
• The password must contain at least 1 letter
• The password must contain at least 1 number

Data provided: “password123”
Expected behavior: The password is accepted

Data provided: “12345”
Expected behavior: The password is not accepted

PHASE 2:

Instead of just rejecting a password, the tool needs to indicate why the password is not acceptable.

Data provided: “12345”
Expected behavior: The tool indicates that the password is not long enough and that the password does not include a letter.

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

class Passwordverifier():

    def verifyPassword(self, password):
        alpha_status = True
        digit_status = True
        
        if len(password) < 8:
            print("Password is less than 8 characters")
            return False

        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            digit_status = False

        if not any(char.isalpha() for char in password):
            print('the password should have at least one character')
            alpha_status = False

        if alpha_status is False or digit_status is False:
            return False

        return True

ob = Passwordverifier()
print(ob.verifyPassword('1111111111'))