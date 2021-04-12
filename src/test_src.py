# author: Denem Orhun

import pytest
import passwordStrengthVerifier

@pytest.fixture
def supply_user():
	user1 = passwordStrengthVerifier.User()

def test1_user_verify_invalid_length():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('abcd1234') is False

def test2_user_verify_valid_length_alphanum():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('abcde12345')

def test3_user_verify_invalid_alpha_missing():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('1111111111111111') is False

def test5_user_verify_invalid_numeric_missing():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('aaaaaaaaaaaaaaaa') is False

def test6_user_verify_uppercase_is_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('ABCD123aeaereareraa')

def test7_user_verify_special_characters_are_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('$$AA11versererss')

def test8_admin_verify_no_special_chars_invalid():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('ABDC23423443dadafdad') is False

def test9_admin_verify_invalid_length():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('abcd1$23') is False

def test10_admin_verify_admin_valid():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('ABDC@!$23423%4')

def test11_verify_blank():
		admin1 = passwordStrengthVerifier.Admin()
		assert admin1._verify_admin_password('               ') is False