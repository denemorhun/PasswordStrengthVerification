# author: Denem Orhun
# ITERATION 4 updating tests

import pytest
import passwordStrengthVerifier

@pytest.fixture
def supply_user():
	user1 = passwordStrengthVerifier.User()

# Test password meets length and alphanum requirements
def test1_verify_length_alphanum_invalid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('abcd1234') is False

# Test password meets length and alphanum requirements
def test2_verify_length_alphanum_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('abcde12345')

# Test password < 8 is False -> negative test case
def test3_admin_does_not_meet_length():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('abcd123') is False

def test3_does_not_meet_alpha():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('1111111111111111') is False

def test4_does_not_meet_numeric():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('aaaaaaaaaaaaaaaa') is False

def test5_verify_uppercase_is_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('ABCD123aeaereareraa')

def test6_verify_special_characters_are_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1._verify_password('$$AA11versererss')

def test7_verify_admin_no_special_chars_is_false():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('ABDC23423443dadafdad') is False

def test8_admin_does_not_meet_length():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('abcd1$23') is False

def test9_verify_admin_valid_password():
	admin1 = passwordStrengthVerifier.Admin()
	assert admin1._verify_admin_password('ABDC@!$23423%4')