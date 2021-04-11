# ITERATION 1 COMMIT

import pytest
import passwordStrengthVerifier

@pytest.fixture
def supply_user():
	user1 = passwordStrengthVerifier.user()

# Test password meets length and alphanum requirements
def test_length_alphanum():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('abcd1234') is True

# Test password < 8 is False -> negative test case
def test_does_not_meet_length():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('abcd123') is False

def test_does_not_meet_alpha():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('11111111') is False

def test_does_not_meet_numeric():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('aaaaaaaa') is False

def test_uppercase_is_valid():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('ABCD123a') is True

def test_special_characters_are_valid():
	user1 = passwordStrengthVerifier.user()
	assert user1.verifyPassword('$$AA11vs') is True


