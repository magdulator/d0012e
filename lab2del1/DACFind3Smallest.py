#tagga inte beat
import random
import time
def main():
    random = generateList(10, 12)
    
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
        return arr
    else:
        h = len(arr)//2

        lst = divideAndFindSmallest(arr[h:]) + divideAndFindSmallest(arr[:h])
        
        minList = []
        tmp = min(lst)
        minList.append(tmp)
        lst.pop(lst.index(tmp))
        tmp = min(lst)
        minList.append(tmp)
        lst.pop(lst.index(tmp))
        tmp = min(lst)
        minList.append(tmp)
        lst.pop(lst.index(tmp))
        return minList
        

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
