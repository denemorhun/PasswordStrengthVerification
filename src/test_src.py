# ITERATION 1 COMMIT

import pytest
import passwordStrengthVerifier

@pytest.fixture
def supply_user():
	user1 = passwordStrengthVerifier.User()

# Test password meets length and alphanum requirements
def test_length_alphanum():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('abcd1234') is True

# Test password < 8 is False -> negative test case
def test_does_not_meet_length():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('abcd123') is False

def test_does_not_meet_alpha():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('11111111') is False

def test_does_not_meet_numeric():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('aaaaaaaa') is False

def test_uppercase_is_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('ABCD123a') is True

def test_special_characters_are_valid():
	user1 = passwordStrengthVerifier.User()
	assert user1.verify_password('$$AA11vs') is True


def test_admin_length():
	admin1 = passwordStrengthVerifier.Admin()
	pass

def test_admin_special_chars():
	admin1 = passwordStrengthVerifier.Admin()
	pass