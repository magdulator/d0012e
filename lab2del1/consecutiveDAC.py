import random
import sys
import time
def main():
    random = generateList(12, 10)
    print(random)
    seconds = time.time()
    if isListAllPositive:
        print(incrementalSubSum)
    else:
        print(consecutiveDAC(random, 0, len(random)-1))
    print(time.time()-seconds)

def generateList(maxNum, length):
    randomList = []
    i = 0
    while i < maxNum:
        n = random.randint(maxNum*-1,maxNum)
        #n = random.randint(1,maxNum)
        if n != 0:
            randomList.append(n) 
            i += 1  
    return randomList

def isListAllPositive(arr):
    for i in arr:
        if arr[i] < 0:
            return False
    return True

def incrementalSubSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


# maxMiddleSum(arr, firstIndex, middleIndex, lastIndex)
# finds the maximum sum in arr[]
def maxMiddleSum(arr, f, m, l):

    # Calculates Maximum sum left side of mid
    tmp = 0
    leftSum = sys.maxsize * -1
    for i in range(m, f-1, -1):
        tmp += arr[i]
        if (tmp > leftSum):
            leftSum = tmp
    
    # Calculates Maximum sum right side of mid
    tmp = 0
    rightSum = sys.maxsize * -1
    for i in range(m + 1, l + 1):
        tmp += arr[i]
        if (tmp > rightSum):
            rightSum = tmp
    #Returns sum of elements on left and right side of mid
    return leftSum + rightSum


# consecutiveDAC(list, firstindex, lastindex)
# returns subarray with maximum sum
#
def consecutiveDAC(arr, f, l):
    if f == l:
        return arr[f]
    else:
        m = int((f + l) / 2)
    return max(consecutiveDAC(arr, f, m), 
               consecutiveDAC(arr, m+1, l),
               maxMiddleSum(arr, f, m, l))
        




main()