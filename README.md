# PasswordStrengthVerification
 App to verify password strength

Run the tests by py.test  -v --junitxml="result.xml" and view the result.xml 

Install the necessary python version 3.6+ and required modules 

attrs==20.3.0
iniconfig==1.1.1
packaging==20.9
pluggy==0.13.1
py==1.10.0
pyparsing==2.4.7
pytest==6.2.3
toml==0.10.2

Ambigious points in the requirement were assumed. 
1) There is a minimum of 10 for standard user, and 13 for admin user, 
but upper limit is not specified. 

2) Required special characters are given but it's unclear whether any other special character is forbidden. 
What should happen if user uses a char not in the given list?

3) The ASCII range of the alphabet supported and foreign language support is not mentioned. 

4) I am assuming obfuscation is out of scope.

5) How to read the password is unclear (i.e. from commandline, from a temp file, from a form, etc)

6) What type of executable (i.e. shell wrapper) for what OS is supported is not mentioned. 

