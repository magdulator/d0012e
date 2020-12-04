import random
import sys

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

def difDivAndCon(arr):
    if len(arr) == 2:
        return arr[1]/arr[0]

    l = len(arr)-1

    if arr[l-1] > arr[l]:
        return difDivAndCon(arr[:l])
    elif arr[0] > arr[1]:
        return difDivAndCon(arr[1:])
    else:
        arr.pop(l-1)
        return difDivAndCon(arr)

        

    



def main():
    random = generateList(12, 12)
    print(random)
    print(difDivAndCon(random))

main()