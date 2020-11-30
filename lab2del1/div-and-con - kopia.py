#tagga inte beat
import random
def main():
    random = generateList(10, 10)
    print(divideAndFindLargest(random))


def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def divideAndFindLargest(randomList):
    if 1 == len(randomList):
        return randomList[0]
    else:
        m = int(len(randomList)/3)
    
        aList = randomList[0:m]
        bList = randomList[m:m*2]
        cList = randomList[m*2:]
        A = divideAndFindLargest(aList)
        B = divideAndFindLargest(bList)
        C = divideAndFindLargest(cList)

        if A < B:
            l = A
            s = B
        else: 
            l = B
            s = A
        if l < C:
            m = l
            l = C
        if m < s:
            return [l, s, m]
        else:
            return [l, m, s]

            





main()