import pytest

##requirement 3
def check_alphabet(s):
    if s.isalpha() == False:
        print("Input contains non-alphabet characters!")
        return 1
    elif s.isalpha()  == True:
        print("You entered valid input!")
        return 2

#test cases
def test_case7():
    assert check_alphabet("876876") == 1

def test_case8():
    assert check_alphabet("*&^&*^") == 1

def test_case9():
    assert check_alphabet("abcd") == 2