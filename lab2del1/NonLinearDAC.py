import random
import sys
import time

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

  
def findBiggestQuota(arr):
    #print(arr)
    if len(arr) == 2:
        if arr[1] > arr[0]:
            return arr[1]/arr[0]
        else:
            return arr[0]/arr[1]

    m=int(len(arr)/2)     # Cut the array into two 
    

    leftBest  = findBiggestQuota(arr[:m])     # assume i and j is in left
    rightBest = findBiggestQuota(arr[m:])    # assume i and j is in the right

    middleBest = max(arr[m:])/min(arr[:m])    #assume i is in the left and j in the right
    
    return max(leftBest, rightBest, middleBest) # returns best of three

def test():
    i = 2
    while i <= 16384:
        random = generateList(30, i)
        starttime = time.time()
        (findBiggestQuota(random))
        timetaken = time.time()
        f = open("myfile.txt", "a")
        f.write(str(i)+" " +str(timetaken-starttime) + "\n")
        f.close()
        i *= 2
        
def main():
    random = generateList(10, 16)
    print(findBiggestQuota(random))
    print(random)
    
    
#test()

main()


# T(1) = 1 , (*)
# T(n) = 2T(n/2) + O(n), when n>2. (**)
#
# T(n) = (**)
# 2T(n/2) + n = (**)
# 2(2(n/4) + n/2 ) + n = 4T(n/4) + 2n = (**)
# 2^k(T(n/2^k)) + kn = (**)

# k = logn

# 2^logn*(T(n/2^logn)) + n*logn= (**)
# n*T(1) + n*logn = n + logn = (**)
#
# ==> O(nlogn) == theta(nlogn)

