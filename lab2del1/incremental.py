import random

def generateList(maxNum, length):
    randomList = []
    for i in range(0, length):
        n = random.randint(0,maxNum)
        randomList.append(n)   
    return randomList

def incrementalAlgo(randomList):
    print(randomList)
    countArray = [0]*(max(randomList)+1) 
    sortedArray = [0]*(len(randomList)+1) 

    for i in range(0, len(randomList)):
        countArray[randomList[i]] += 1
    print("Occurrencies for each index:            ", countArray)

    for i in range(0, len(countArray)-1):
        countArray[i+1] = countArray[i] + countArray[i + 1]
    print("Add occurrency with previous occurency: ", countArray)

    for i in range(0, len(randomList)):
        putInList = randomList[i]
        sortedArray[countArray[putInList]] = putInList
        countArray[putInList] -= 1
    del(sortedArray[0])
    print(sortedArray)

def main():
    random = generateList(10, 10)
    incrementalAlgo(random)

main()