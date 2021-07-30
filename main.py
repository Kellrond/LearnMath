from math import ceil
from random import randrange
from time import time

# Game variables
level = 1
correct = 0
rounds = 0
totalDuration = 0
startTimer = time()

def setDigits(difficulty):
    varALevel= 0
    varBLevel = 0
    count = 0
    while count < difficulty:
        if singleVariableInc and count != 0: 
            if count % 2 == 1 and count != 0:
                varALevel += 1
            elif count % 2 == 0 and count != 1:
                varBLevel += 1           
        elif count != 0:
            varALevel += 1
            varBLevel += 1
        count += 1   
    minA = 10 ** varALevel
    maxA = 10 ** (varALevel + 1)
    minB = 10 ** varBLevel
    maxB = 10 ** (varBLevel + 1)
    return [minA, maxA, minB, maxB]

def validateInt(text):
    print(text, end=" ")
    fail = True
    while fail:
        entry = input()
        try:
            output = int(entry.strip())
            fail = False
        except:
            print("Please input a whole number:", end=" ")
    return output

# Game settings
roundsToAdvance = validateInt("No. of correct rounds before advancing:")
gameDuration = validateInt("Duration of game in minutes:")
singleVariableInc = True
sglVarDifficultyOffset = 0

while totalDuration < gameDuration:
    difficulty = ceil(level / roundsToAdvance) 
    minA, maxA, minB, maxB = setDigits(difficulty)

    a = randrange(minA, maxA)
    b = randrange(minB, maxB) 
    c = a * b

    answer = validateInt("%s x %s =" % (a, b))

    if answer == c:
        print("Correct")
        correct += 1
        level += 1
    else:
        print("Incorrect: %s" % c)
        level -= 3
        level = level * 1 
    rounds += 1 
    totalDuration = (time() - startTimer) / 60

print("Completed %s rounds in %s minutes" % (rounds, totalDuration))
print("%s correct and %s incorrect %s percentage correct" % (correct, rounds - correct, "{:.1%}".format(correct / rounds)))
