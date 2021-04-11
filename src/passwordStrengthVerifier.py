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

'''


def verifyPassword(password):
    hasDigit=False
    hasAlpha=False
  
    # for checking if password length
    if len(password) < 8:
        return False
  
    # check if password contains at least 1 letter and 1 number
    else:
	    for i in password:
		    if i.isdigit():
		        hasDigit = True
		    if i.isalpha():
		        hasAlpha = True
		    if hasAlpha and hasDigit:
			    return True

    return False

print(verifyPassword('111111111'))