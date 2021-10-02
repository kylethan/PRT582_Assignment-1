import pytest

##Requirement 1
def calculate_score(s):
    
    SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
            "x": 8, "z": 10}
    total = 0
    for letter in s:
        total += SCORES[letter]
        print("letter " + letter + " has " + str(SCORES[letter]) + " points.")
    print("Your total score is calculated by adding the scores from the each letter in the alphabet: ", total)

    return total

##Test cases
def test_case1():
    assert calculate_score("cabbage") == 14

def test_case2():
    assert calculate_score("yes") == 6

def test_case3():
    assert calculate_score("money") == 10
