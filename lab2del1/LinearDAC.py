import random
import sys
import time

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

<<<<<<< Updated upstream
def difDivAndCon(arr, smallestNum):
    
    if len(arr) == 1:
        smallestNum = arr[0]
        return 0
    else:
        if (arr[0] < smallestNum):
            smallestNum = arr[0]
=======
def difDivAndCon(arr):
    if len(arr) == 2:
        return arr[1]/arr[0]
>>>>>>> Stashed changes

    l = len(arr)-1

    if arr[l-1] > arr[l]:
        return difDivAndCon(arr[:l])
    elif arr[0] > arr[1] or arr[0] > arr[l-1]:
        return difDivAndCon(arr[1:])
    else:
        arr.pop(l-1)
        return difDivAndCon(arr)

 

def main():

    sys.setrecursionlimit(sys.maxsize) 
<<<<<<< Updated upstream
    random = generateList(20, 4)
    random = [11, 2, 7, 6]
=======
    random = generateList(10, 16)
>>>>>>> Stashed changes
    print(random)


    starttime = time.time()
    print(difDivAndCon(random))
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
