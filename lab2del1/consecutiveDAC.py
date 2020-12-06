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
        n = random.randint(maxNum*-1,maxNum) #Både positiva och negativa tal generator
        #n = random.randint(1,maxNum) #Bara positiva tal generator
        if n != 0:
            randomList.append(n) 
            i += 1  
    return randomList

#Checks if all numbers in list is a positive number
def isListAllPositive(arr):
    for i in arr:
        if arr[i] < 0:
            return False
    return True
#Adderar alla tal i en lista till en summa
#Time complexity O(n)
def incrementalSubSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# based on https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
# maxMiddleSum(arr, firstIndex, middleIndex, lastIndex)
# finds the maximum sum in arr[]
# Time complexity O(n)
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
# Time Complexity O(n*log(n))
def consecutiveDAC(arr, f, l):
    if f == l:
        return arr[f]
    else:
        m = int((f + l) / 2)
    return max(consecutiveDAC(arr, f, m),    #Case 1: subarray is in lowerhalf of list
               consecutiveDAC(arr, m+1, l),  #Case 2: subarray is in higherhalf of list
               maxMiddleSum(arr, f, m, l))   #Case 3: subarray is in split between higher and lower of list
        




main()