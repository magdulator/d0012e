import random
import sys
import time

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

def difDivAndCon(arr):
    if len(arr) == 2:
        return arr[1]/arr[0]

    l = len(arr)-1

def findMaximumQuote(arr):
    if 2 == len(arr):
        return arr[1]/arr[0], arr[0], arr[1]
    else: 
        h = len(arr)//2
        
        (rightQuote, minRight, maxRight) = findMaximumQuote(arr[h:]) # Case 1: in the right
        (leftQuote, minLeft, maxLeft) = findMaximumQuote(arr[:h]) # Case 2: in the right side
        result = max(rightQuote, leftQuote, max(minRight, maxRight)/min(minLeft, maxLeft))

        if arr.index(maxLeft) > arr.index(minLeft):
            result = max(result, maxLeft/minLeft)
        if arr.index(maxRight) > arr.index(minRight):
            result = max(result, maxRight/minLeft)
        return result, min(minLeft, minRight, maxRight, maxLeft), max(maxLeft, maxRight, minLeft, minRight), 
        


def main():

    sys.setrecursionlimit(sys.maxsize) 
    random = generateList(20, 8)
    print(random)


    starttime = time.time()
    print(findMaximumQuote(random))
    print(time.time() - starttime)
main()

