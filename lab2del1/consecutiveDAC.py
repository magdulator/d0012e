import random
import sys
import time
import math
def main():
    random = generateList(2, 8)
    print(random)
    seconds = time.time()
    if isListAllPositive(random):
        print(incrementalSubSum(random, 0))
    else:
        print(consecutiveDAC(random, 0, len(random)-1))
    print(time.time()-seconds)

def generateList(maxNum, length):
    randomList = []
    i = 0
    while i < length:
        n = random.uniform(maxNum*-1, maxNum) #Både positiva och negativa tal generator
        #n = random.uniform(0, maxNum) #Bara positiva tal generator
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
def incrementalSubSum(arr, maxProduct):
    if len(arr) == 0:
        return (0, arr, 0)
        
        
        




        


# based on https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
# maxMiddleSum(arr, firstIndex, middleIndex, lastIndex)
# finds the maximum sum in arr[]
# Time complexity O(n)
def maxMiddleSum(arr, f, m, l):

    # Calculates the product of left side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    posBottom = 0
    negBottom = 0
    left = 1
    positiveLeft = 1
    negativeLeft = 1
    for i in range(m, f-1, -1):
        left *= arr[i]
        if left > 0 and positiveLeft < left:
            positiveLeft = left
            posBottom = i
        elif negativeLeft > left:
            negativeLeft = left
            negBottom = i
    
    # Calculates the product of right side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    posTop = 0
    negTop = 0
    right = 1
    positiveRight = 0
    negativeRight = 0
    for i in range(m + 1, l + 1):
        right *= arr[i]
        if right > 0 and positiveRight < right:
            positiveRight = right
            posTop = i+1
        elif negativeRight > right:
            negativeRight = right
            negTop = i+1
    
    positive = positiveRight*positiveLeft
    negative = negativeLeft*negativeRight
    if negative > positive:
        return negative, arr[negBottom:negTop]
    else:
        return positive, arr[posBottom:posTop]


# consecutiveDAC(list, firstindex, lastindex)
# returns subarray with maximum sum
# Time Complexity O(n*log(n))
def consecutiveDAC(arr, f, l):
    if f == l:
        return arr[f], arr
    else:
        m = int((f + l) / 2)
        return max(consecutiveDAC(arr, f, m),    #Case 1: subarray is in lowerhalf of list
               consecutiveDAC(arr, m+1, l),  #Case 2: subarray is in higherhalf of list
               maxMiddleSum(arr, f, m, l))   #Case 3: subarray is in split between higher and lower of list
    
    
        




main()