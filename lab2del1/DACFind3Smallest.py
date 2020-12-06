#tagga inte beat
import random
import time
def main():
    random = generateList(10, 4)
    
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
def divideAndFindSmallest(randomList):
    if randomList[0] <= randomList[1] <= randomList[2] and len(randomList) <= 3:
        return randomList
    else:
        m = int(len(randomList)-1)
        
        if randomList[m] < randomList[0]:
            return divideAndFindSmallest([randomList[m]] + randomList[:m])
        elif randomList[m] < randomList[1]:
            return divideAndFindSmallest([randomList[0]] + [randomList[m]] + randomList[1:m])
        elif randomList[m] < randomList[2]:
            return divideAndFindSmallest(randomList[0:2] + [randomList[m]] + randomList[2:m])
        else:
            randomList.pop(m)
            return divideAndFindSmallest(randomList)


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
