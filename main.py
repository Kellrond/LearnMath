from math import ceil
from random import randrange
from datetime import date, datetime
from time import time
import json

# Game variables
level = 1
correct = 0
rounds = 0
totalDuration = 0
sglVarDifficultyOffset = 0
levelsToDecrease = 2

# Game settings
operatorList = ["+", "-", "*", "/"]
operatorString = ", ".join(operatorList)

def calculate(a, b, operator):
    string = "%s%s%s" % (a, operator, b)
    c = eval(string)
    return c

def scoreAnswer(answer, c, level, correct):
    if answer == c:
        print("Correct")
        correct += 1
        level += 1
    else:
        print("Incorrect: %s" % c)
        correct = 0
        level -= levelsToDecrease
    return correct, level

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
        entry = input().strip()
        try:
            output = int(entry)
            fail = False
        except:
            print("Please input a whole number:", end=" ")
    return output

def validateOperator(text):
    print(text, end=" ")
    fail = True
    while fail:
        entry = input().strip()
        if entry in operatorList:
            output = entry
            fail = False
        else:
            print("Please input on operator %s:" % operatorString, end=" ")
    return output

# User settings
operator = validateOperator("What operator %s:" % operatorString)
roundsToAdvance = validateInt("No. of correct rounds before advancing:")
gameDuration = validateInt("Duration of game in minutes:")
singleVariableInc = True

startTimer = time()
while totalDuration < gameDuration:
    difficulty = ceil(level / roundsToAdvance) 
    minA, maxA, minB, maxB = setDigits(difficulty)
    a = randrange(minA, maxA)
    b = randrange(minB, maxB) 
    c = calculate(a, b, operator)
    answer = validateInt("%s %s %s =" % (a, operator, b))
    correct, level = scoreAnswer(answer, c, level, correct)
    rounds += 1 
    totalDuration = (time() - startTimer) / 60

print("Completed %s rounds in %s minutes" % (rounds, totalDuration))
print("%s correct and %s incorrect %s percentage correct" % (correct, rounds - correct, "{:.1%}".format(correct / rounds)))

log = {
    'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d'),
    'operator': operator,
    'roundsToAdvance': roundsToAdvance,
    'gameDuration': gameDuration,
    'singleVariableInc': singleVariableInc,
    'level': level,
    'rounds': rounds,
    'correct': correct
}

with open('log.json', 'a') as file:
    jsonLog = json.dumps(log)
    file.write(jsonLog + "\n")    
