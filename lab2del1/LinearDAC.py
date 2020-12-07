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
        
        (rightQuote, minRight, maxRight) = findMaximumQuote(arr[h:]) # Case 1: in the left side
        (leftQuote, minLeft, maxLeft) = findMaximumQuote(arr[:h]) # Case 2: in the right side
        (middleQuote, minMiddle, maxMiddle) = findQuoteMiddle(minLeft, maxLeft, minRight, maxRight)
        if (arr.index(minMiddle) > arr.index(maxMiddle)):
            middleQuote = max(rightQuote, leftQuote)
        return max(maxLeft/minLeft, maxRight/minRight, middleQuote, rightQuote, leftQuote), minMiddle, maxMiddle
        
def findQuoteMiddle(a, b, c, d):
    return max(a,b,c,d)/min(a,b,c,d)

def main():

    sys.setrecursionlimit(sys.maxsize) 
    random = generateList(10, 16)
    print(random)


    starttime = time.time()
    print(difDivAndCon(random))
    print(time.time() - starttime)
main()

