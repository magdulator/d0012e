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
    
    if len(arr) == 2:
        smallestNum = max(arr[1], arr[0])
        return arr[1]/arr[0]
    else:
        if (arr[0] < smallestNum):
            smallestNum = arr[0]

        quota = difDivAndCon(arr[1:], smallestNum)

        if (arr[0]/smallestNum > quota ):
            return arr[0]/smallestNum
        else:
            return quota
        
        
        

def main():

    sys.setrecursionlimit(sys.maxsize) 
    random = generateList(20, 16)
    print(random)


    starttime = time.time()
    print(difDivAndCon(random, sys.maxsize))
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
