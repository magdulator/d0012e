import random
import sys
import time

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

def difDivAndCon(arr, smallestNum):
    

    if len(arr) == 0:
        return 0
    else:
        tmp = smallestNum
        if (arr[0] < smallestNum):
            smallestNum = arr[0]

        if (arr[0]/tmp > difDivAndCon(arr[1:], smallestNum) ):
            return arr[0]/tmp
        
        else:
            return difDivAndCon(arr[1:], smallestNum)

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
    random = generateList(20, 8)
    print(random)


    starttime = time.time()
    #print(difDivAndCon(random, sys.maxsize))
    print(findMaximumQuote(random))
    print(time.time() - starttime)
main()


# T(2) = 1 , (*)
# T(n) = 3 + T(n-1), when n>2. (**)
#
# T(n) = (**)
# 3 + T(n-1) = (**)
# 3 + ( 3 + T(n-2)) = 6 + T(n-2) = (**)
# 3k + T(n-k) = .. = 3(n-2) + T(2) = 3n - 5
#  
# ==> O(n)
