class Heap:
    ################################################################
    # Heap constructor
    def __init__(self, capacity):
        self.heap = []            #Heap List
        self.Edgelist = []        #List of corresponding edges
        self.currentSize = 0      #Current size of heap list
        self.capacity = capacity  #Max Capacity of the heap list

    
    ################################################################
    # Inserts weight and corresponding edge
    # cost: O(c)
    def insert(self, weight, edge):
        if self.isFull():
            print("Heap is full")
        else:
            self.heap.append(weight)
            self.Edgelist.append(edge)
            self.fixHeap(self.currentSize)
            self.currentSize += 1


    ################################################################
    # sorts the list 
    # cost: O(n)
    def fixHeap(self, index):
        newValue = self.heap[index]
        newEdge = self.heap[index]

        while (index > 0 and newValue > self.heap[self.getParent(index)]):
            parentIndex = self.getParent(index)
            self.heap[index] = self.heap[parentIndex]
            self.Edgelist[index] = self.Edgelist[parentIndex]
            index = self.getParent(index)
        
        self.heap[index] = newValue
        self.Edgelist[index] = newEdge


    ################################################################
    # Checks if heap is full returns true if true
    # cost: O(c)
    def isFull(self): 
        return self.currentSize == self.capacity
    

    ################################################################
    # Retuns parent's index
    # cost: O(c)
    def getParent(self, index):
        return int((index-1)/2)

    def printHeap(self):
        for i in range(self.currentSize):
            print (self.heap[i], self.Edgelist[i])
    


""" 
lst = [2, 3, 1]
lst2 = ['a', 'b', 'c']

h = Heap(3)

for i in range(3):
    h.insert(lst[i], lst2[i])
    print(lst[i], lst2[i])

print(h.printHeap())
 """