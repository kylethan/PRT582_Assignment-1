import pytest
import enchant 

#requirement 5
def dictionary_check(s):
    d = enchant.Dict("en_US")
    while d.check(s) == False:
        print("\n" + s + " is not an English word!")
        s = input("Please enter a valid word: ")
    else:
        print("\n" + s + " is an English word")
    return s

#test cases
def test_case14():
    assert dictionary_check("key")

def test_case15():
    assert dictionary_check("abcd")
