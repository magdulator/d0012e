import random
import sys
import time
def main():
    random = generateList(12, 6)
    print(random)
    seconds = time.time()
    print(consecutiveDAC(random))
    secondsafter = time.time()
    resulttime = secondsafter - seconds 
    print(resulttime)

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def consecutiveDAC(arr):
    if 



