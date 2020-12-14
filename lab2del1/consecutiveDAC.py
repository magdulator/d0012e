import random
import sys
import time
def main():
    random = generateList(10, 5)
    print(random)
    seconds = time.time()
    if isListAllPositive(random):
        print(incrementalSubSum(random))
    else:
        print(consecutiveDAC(random, 0, len(random)-1))
    print(time.time()-seconds)

def generateList(maxNum, length):
    randomList = []
    i = 0
    while i < length:
        n = random.randint(maxNum*-1,maxNum) #Både positiva och negativa tal generator
        #n = random.randint(1,maxNum) #Bara positiva tal generator
        if n != 0:
            randomList.append(n) 
            i += 1  
    return randomList

#Checks if all numbers in list is a positive number
def isListAllPositive(arr):
    key = True
    for i in arr:
        if i < 0:
            key = False
    return key
#Adderar alla tal i en lista till en summa
#Time complexity O(n)
def incrementalSubSum(arr):
    if len(arr) == 0:
        return 1
    else:
        return incrementalSubSum(arr[1:]) * arr[0]

# based on https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
# maxMiddleSum(arr, firstIndex, middleIndex, lastIndex)
# finds the maximum sum in arr[]
# Time complexity O(n)
def maxMiddleSum(arr, f, m, l):

    # Calculates the product of left side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    left = 1
    positiveLeft = 1
    for i in range(m, f-1, -1):
        left *= arr[i]
        if left > 0:
            positiveLeft = left
    
    # Calculates the product of right side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    right = 1
    positiveRight = 1
    for i in range(m + 1, l + 1):
        right *= arr[i]
        if right > 0:
            positiveRight = right

    return max(positiveRight*positiveLeft, left*right)


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