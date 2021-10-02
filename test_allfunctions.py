import pytest
import time
import random
import function1
import function2
import function3
import function4
import function5
import assignment1

##PLEASE DISABLE OTHER TEST CASES OF OTHER REQUIREMENTS IF YOU WANT TO TEST ANY SPECIFIC REQUIREMENT.
##Test cases for function 1##
def test_case1():
    assert function1.calculate_score("cabbage") == 14

def test_case2():
    assert function1.calculate_score("yes") == 6

def test_case3():
    assert function1.calculate_score("money") == 10

##Test cases for function 2##
def test_case4():
    assert function2.uppercase_lowercase("MONEY") == "money"
    print("test successfully! MONEY change to money")

def test_case5():
    assert function2.uppercase_lowercase("FrienD") == "friend"
    print("test successfully! FrienD change to friend")

def test_case6():
    assert function2.uppercase_lowercase("NumBer") == "number"
    print("test successfully! NumBer change to number")

##Test cases for function 3##
def test_case7():
    assert function3.check_alphabet("876876") == 1

def test_case8():
    assert function3.check_alphabet("*&^&*^") == 1

def test_case9():
    assert function3.check_alphabet("abcd") == 2

##Test cases for function 4##
def test_case10():
    assert len(function4.input_score("monitor"))

def test_case11():
    time.sleep(5)
    random.seed(4)
    assert len(function4.input_score("best"))

def test_case12():
    random.seed(7)
    assert len(function4.input_score("yes")) 

def test_case13():
    time.sleep(12) 

##Test cases for function 5##
def test_case14():
    assert function5.dictionary_check("key")

def test_case15():
    assert function5.dictionary_check("abcd")

##test cases for the whole program##
def test_case14():
    random.seed(4)
    assignment1.scrabble("BEST")

def test_case15():
    assignment1.scrabble("abcd")