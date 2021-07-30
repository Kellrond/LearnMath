from random import random, randrange
from time import time

wins = 0
roundsToAdvance = 5
singleVariableInc = True
duration = 5

start = time.time()
while True:
    difficulty = int(wins / roundsToAdvance)
    maxDigits = 10 ** (difficulty + 1)
    a = randrange(1, maxDigits)
    if difficulty % 2 == 1 and singleVariableInc:
        b = randrange(1, maxDigits / 10) 
    else:
        b = randrange(1, maxDigits)
    c = a * b
    print("%s x %s =" % (a, b), end=" ")
    answer = int(input())
    if answer == c:
        print("Correct")
        wins += 1
    else:
        print("Incorrect: %s" % c)
        wins -= 3
        wins = wins * 1 