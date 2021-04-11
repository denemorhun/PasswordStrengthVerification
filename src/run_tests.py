import passwordStrengthVerifier

user1 = passwordStrengthVerifier.User()
user1.is_pwd_valid(user1._verify_password('111111111111'))
user1.is_pwd_valid(user1._verify_password('8888dddd'))
user1.is_pwd_valid(user1._verify_password('        '))
user1.is_pwd_valid(user1._verify_password('uiurerererare'))
user1.is_pwd_valid(user1._verify_password('ADERE3232425'))
user1.is_pwd_valid(user1._verify_password('@#$@#$#@$@$$@$@'))
user1.is_pwd_valid(user1._verify_password('@#$@$@ADAFDAF23423424'))
user1.is_pwd_valid(user1._verify_password('111111111111'))


admin1 = passwordStrengthVerifier.Admin()
admin1.is_pwd_valid(admin1._verify_admin_password('111'))
admin1.is_pwd_valid(admin1._verify_admin_password('111111111@11111111'))
admin1.is_pwd_valid(admin1._verify_admin_password('@1111dddddddddddd'))
admin1.is_pwd_valid(admin1._verify_admin_password('ABDC23423443dadafdad'))
