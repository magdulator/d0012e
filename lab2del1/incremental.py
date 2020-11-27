import random

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def incrementalAlgo(randomList):
    #sort by some algorithm
    print(randomList)

def main():
    random = generateList(10, 10)
    incrementalAlgo(random)

main()