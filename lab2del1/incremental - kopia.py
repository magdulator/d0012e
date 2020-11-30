import random
import sys
def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def incrementalAlgo(randomList):
    print(randomList)
    result = [sys.maxsize]*3
    for i in randomList:
        if i > result[0]:
            result = [i,result[0],result[1]]
        elif i > result[1]: 
            result = [result[0],i,result[1]]
        elif i > result[2]:
            result = [result[0],result[1],i]
    return result


def main():
    random = generateList(10, 10)
    print(incrementalAlgo(random))

main()