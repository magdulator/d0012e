import random
import sys
import time

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1,maxNum)
        randomList.append(n)   
    return randomList

#https://stackoverflow.com/questions/40503101/divide-and-conquer-to-find-maximum-difference-in-an-array
#T(n) = 2T(n/2) + O(n)
#T(n) = O(nlogn)
  
def DivideAndConquerQ(arr):
    if len(arr) <= 1:
        return 0

    mid=int(len(arr)/2)
    # Cut the array into two 
    left  = arr[0:mid]
    right = arr[mid:]

    # assume i and j is in left and i and j is in right seperately
    leftBest  = DivideAndConquerQ(left)
    rightBest = DivideAndConquerQ(right)

    #assume i in left and j in right
    crossBest = max(right)/min(left)

    # Return the best of the three

    return max(leftBest, rightBest, crossBest)

def test():
    i = 0
    while i <= 5001:
        random = generateList(30, i)
        starttime = time.time()
        (DivideAndConquerQ(random))
        timetaken = time.time()
        f = open("myfile.txt", "a")
        f.write(str(i)+" " +str(timetaken-starttime) + "\n")
        f.close()
        i += 200
        
def main():
    test()

main()