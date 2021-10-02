import random
import enchant
import time
import threading
import pytest

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
          "x": 8, "z": 10}

def countdown():
    global t
    t = 16
    for x in range(16):
        t = t - 1
        time.sleep(1)
    print("\nYour time is up!")
    print("You failed!!")
    return print
countdown_thread = threading.Thread(target=countdown)
countdown_thread.daemon = True
countdown_thread.start()

def scrabble(s):
    while t > 0: 
        print("You have " + str(t) + " seconds to answer the question.")
        total = 0
        ran = random.randint(1,13)
        d = enchant.Dict("en_US")
        s = s.lower()
        if t == 0:
            break
        while s.isalpha() == False or len(s) != ran or d.check(s) == False:
            if s.isalpha() == False and len(s) != ran:
                print("You have " + str(t) + " second left")
                print("Your input contains non-alphabet characters and the length is not equal to the required length.")
                s = input("Type a valid word with " + str(ran) + " letters: ").lower()
            elif s.isalpha() == False:
                print("You have " + str(t) + " second left")
                print("Your input contains non-alphabet characters.")
                s = input("Type a valid word with " + str(ran) + " letters: ").lower()
            elif len(s) != ran:
                print("You have " + str(t) + " second left")
                print("Your input length is not equal to required length.")
                s = input("Type a valid word with " + str(ran) + " letters: ").lower()
            elif d.check(s) == False:
                print("You have " + str(t) + " second left")
                print("Your word is not an English word.")
                s = input("Type a valid word with " + str(ran) + " letters: ").lower()
            if t == 0:
                break
        if t == 0:
            break
        total = total + t
        saving = total
        for letter in s:
            total += SCORES[letter]
            print("letter " + letter + " has " + str(SCORES[letter]) + " points.")
        print("Your score is calculated by adding the time remaining (" + str(saving) +") and the scores from the alphabet: ", total)
        break
    return s    

def test_case16():
    random.seed(4)
    scrabble("BEST")

def test_case17():
    scrabble("abcd")




    



