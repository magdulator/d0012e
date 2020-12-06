import random
import math

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList
  

def incrementalAlgo(randomList):
    print(randomList)
    minList = [math.inf]*3
    
    if len(randomList) < 3:
        return "List too small"    
    
    for i in range(len(randomList)):
        current = randomList[i]

        if(current < minList[0]):
            minList = [current, minList[0], minList[1]]
            
        elif(current < minList[1]):
            minList = [minList[0], current, minList[1]]

        elif(current < minList[2]):
            minList[2] = current
    print (minList)

def main():
    random = generateList(20, 10)
    incrementalAlgo(random)

main()

# W(3) = 3
# W(n) = 3(n-3) = 3n - 9, n>3

# 3n -9 = O(n)
