#tagga inte beat
import random
import time
import math
def main():
    random = generateList(100, 24)
    print(random)
    seconds = time.time()
    
    print(divideAndFindSmallest(random))
    secondsafter = time.time()
    resulttime = secondsafter - seconds 
    print(resulttime)

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList
#######################################################
#Finds the 3 smallest values in a list.
#Time Complexity = O(n)
def divideAndFindSmallest(arr):
    if len(arr) == 3:
        r = [math.inf]*3
        for i in range(len(arr)):
            current = arr[i]
            if(current < arr[0]):
                r = [current, r[0], r[1]]

            elif(current < arr[1]):
                r = [r[0], current, r[1]]

            elif(current < arr[2]):
                r = [r[1], r[2], current]
        return r
        

    else:
        h = len(arr)//2

        lst = divideAndFindSmallest(arr[h:]) + divideAndFindSmallest(arr[:h])
        
        arr = []
        tmp = min(lst)
        arr.append(tmp)
        lst.pop(lst.index(tmp))
        tmp = min(lst)
        arr.append(tmp)
        lst.pop(lst.index(tmp))
        tmp = min(lst)
        arr.append(tmp)
        lst.pop(lst.index(tmp))
        return arr
        

main()


# T(3) = 3 , (*)
# T(n) = 3 + T(n-1), when n>3. (**)
#
# T(n) = (**)
# 3 + T(n-1) = (**)
# 3 + ( 3 + T(n-2)) = 6 + T(n-2) = (**)
# 3k + T(n-k) = .. = 3(n-3) + T(3) = 3n -9
#  
# ==> O(n)
