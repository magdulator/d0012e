import random
import sys
import time
def main():
#    random = generateList(10, 5)
    random = [0.5, 0.9, 7, 0.7, 0.5, 5, 0.1, 6, 0.9, 2, 0.1, 1000, 0.5, 2.7]
    print(random)
    seconds = time.time()
    if isListAllPositive(random):
        print(incrementalSubSum(random, 0, [], 1, []))
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


# arr = arr
# maxSoFar = (håller koll på det största man har fått)
# MaxList = subarray
# Temp = Används när man får ett mindre tal för att kolla vidare från den för att
# se om man får ett bättre resultat senare
# TempList = Listan som fortsätter gå till den är mindre än 1

def incrementalSubSum(arr, maxSoFar, MaxList, Temp, Templist):
    if len(arr) == 0:
        return maxSoFar, MaxList
    else:
        
        Templist.append(arr[0])
        Temp = Temp*arr[0]

        if Temp > maxSoFar:
            MaxList = Templist[:]
            maxSoFar = Temp

        if Temp < 1:
            Temp = 1
            Templist = []

        return incrementalSubSum(arr[1:], maxSoFar, MaxList, Temp, Templist)


# based on https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
# maxMiddleSum(arr, firstIndex, middleIndex, lastIndex)
# finds the maximum sum in arr[]
# Time complexity O(n)
def maxMiddleSum(arr, f, m, l):

    # Calculates the product of left side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    left = 1
    positiveLeft = 1
    negativeLeft = 1
    for i in range(m, f-1, -1):
        left *= arr[i]
        if left > 0:
            positiveLeft = left
        else:
            negativeLeft = left
    
    # Calculates the product of right side
    # Keeps a copy of positive product incase uneven amount of negative numbers
    right = 1
    positiveRight = 1
    negativeRight = 1
    for i in range(m + 1, l + 1):
        right *= arr[i]
        if right > 0:
            positiveRight = right
        else:
            negativeRight = right

    return max(positiveRight*positiveLeft, left*right, negativeLeft*negativeRight)


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
