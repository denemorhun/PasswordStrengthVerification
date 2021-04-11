# ITERATION 3 Commit

import pytest
import passwordStrengthVerifier

@pytest.fixture
def supply_user():
	user1 = passwordStrengthVerifier.User()

# Test password meets length and alphanum requirements
def test1_length_alphanum():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('abcd1234')

# Test password < 8 is False -> negative test case
def test2_does_not_meet_length():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('abcd123') is False

def test3_does_not_meet_alpha():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('11111111') is False

def test4_does_not_meet_numeric():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('aaaaaaaa') is False

def test5_verify_uppercase_is_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('ABCD123a')

def test6_verify_special_characters_are_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('$$AA11vs') 

def test7_verify_admin_no_special_chars():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1.verify_admin_password('ABDC23423443dadafdad') is False

def test8_admin_does_not_meet_length():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1.verify_admin_password('abcd1$23') is False

def test9_verify_admin_special_chars():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1.verify_admin_password('ABDC@!$234234')


	''' Phase 3 output:

	platform darwin -- Python 3.9.0, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /Users/dorhun/Documents/GitHub/PasswordStrengthVerification/env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/dorhun/Documents/GitHub/PasswordStrengthVerification/src
collected 9 items                                                                                                                                    

test_src.py::test1_length_alphanum PASSED                                                                                                      [ 11%]
test_src.py::test2_does_not_meet_length PASSED                                                                                                 [ 22%]
test_src.py::test3_does_not_meet_alpha PASSED                                                                                                  [ 33%]
test_src.py::test4_does_not_meet_numeric PASSED                                                                                                [ 44%]
test_src.py::test5_verify_uppercase_is_valid PASSED                                                                                            [ 55%]
test_src.py::test6_verify_special_characters_are_valid PASSED                                                                                  [ 66%]
test_src.py::test7_verify_admin_no_special_chars PASSED                                                                                        [ 77%]
test_src.py::test8_admin_does_not_meet_length PASSED                                                                                           [ 88%]
test_src.py::test9_verify_admin_special_chars PASSED                                                                                           [100%]

================================================================= 9 passed in 0.09s ==================================================================
(env) bash-3.2$ 

'''