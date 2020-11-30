#tagga inte beat
import random
def main():
    random = generateList(12, 12)
    print(random)
    print(divideAndFindLargest(random))


def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def divideAndFindLargest(randomList):
    if 3 == len(randomList):
        if randomList[1] < randomList[0]:
            randomList = [randomList[1], randomList[0], randomList[2]]
        if randomList[2] < randomList[1]:
            randomList = [randomList[0], randomList[2], randomList[1]]
        if randomList[1] < randomList[0]:
            randomList = [randomList[1], randomList[0], randomList[2]]
        return randomList
    else:
        m = int(len(randomList)/2)
    

        aList = randomList[0:m]
        bList = randomList[m:]
        A = divideAndFindLargest(aList)
        B = divideAndFindLargest(bList)

        for i in A: #always loops 3 times 
            if i <= B[0]:
                B = [i,B[0],B[1]]
            elif i <= B[1]: 
                B = [B[0],i,B[1]]
            elif i <= B[2]:
                B = [B[0],B[1],i]
        return B
        





main()
