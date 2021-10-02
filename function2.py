##Requirement 2

import pytest

def uppercase_lowercase(s):
   
    a = s.lower()

    return a

##test cases
def test_case4():
    assert uppercase_lowercase("MONEY") == "money"
    print("test successfully! MONEY change to money")

def test_case5():
    assert uppercase_lowercase("FrienD") == "friend"
    print("test successfully! FrienD change to friend")

def test_case6():
    assert uppercase_lowercase("NumBer") == "number"
    print("test successfully! NumBer change to number")