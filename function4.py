from itertools import count
import pytest
import time
import random
import threading

##requirement 4

#countdown timer
def countdown():
    global t
    t = 16
    for x in range(16):
        t = t - 1
        time.sleep(1)
    print("\nYour time is up!")
    print("You failed!!")
    
countdown_thread = threading.Thread(target=countdown)
countdown_thread.daemon = True
countdown_thread.start()

#length check and score calculation with extra mark from time remaining
def input_score(s):
    SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
            "x": 8, "z": 10}
    ran = random.randint(1,13)
    global total
    total = 0 
    print("\nThe random number is: " + str(ran))
    if len(s) != ran:
        print("Your length is not equal to the requirement")
        return s
    elif len(s) == ran:
        print("your length is equal to the requirement")
        total = total + t
        saving = total
        for letter in s:
            total += SCORES[letter]
            print("letter " + letter + " has " + str(SCORES[letter]) + " points.")
        print("The remaining time is: "+ str(t))
        print("Your score is calculated by adding the time remaining (" + str(saving) +") and the scores from the alphabet: ", total)
        return s

#test cases
def test_case10():
    assert len(input_score("monitor"))

def test_case11():
    time.sleep(5)
    random.seed(4)
    assert len(input_score("best"))
    assert total == 17

def test_case12():
    random.seed(7)
    assert len(input_score("yes")) 

def test_case13():
    time.sleep(12)
    
    
    
    