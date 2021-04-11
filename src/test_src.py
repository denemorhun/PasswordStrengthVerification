# ITERATION 1 COMMIT

from passwordStrengthVerifier import verifyPassword

# Test password meets length and alphanum requirements
def test_length_alphanum():
	assert verifyPassword('abcd1234') is True

# Test password < 8 is False -> negative test case
def test_does_not_meet_length():
	assert verifyPassword('abcd123') is False
def test_does_not_meet_alpha():
	assert verifyPassword('11111111') is False

def test_does_not_meet_numeric():
	assert verifyPassword('aaaaaaaa') is False

def test_uppercase():
	assert verifyPassword('ABCD123a') is True
