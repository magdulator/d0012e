class heap:
    ################################################################
    # Heap constructor
    def __init__(self, capacity):
        self.heap = []            #Heap List
        self.currentSize = 0      #Current size of heap list
        self.capacity = capacity  #Max Capacity of the heap list

    
    ################################################################
    # Inserts input at the last position
    # O(c) cost
    def insert(self, input):
        if self.isFull():
            print("Heap is full")
        else:
            self.heap.append(input)
            self.fixHeap(self.currentSize)
            self.currentSize += 1


    ################################################################
    # sorts the list 
    # O(n)
    def fixHeap(self, index):
        newValue = self.heap[index]

        while (index > 0 and newValue > self.heap[self.getParent(index)]):
            self.heap[index] = self.heap[self.getParent(index)]
            index = self.getParent(index)
        
        self.heap[index] = newValue


    ################################################################
    # Checks if heap is full returns true if true
    # O(c) cost
    def isFull(self): 
        return self.currentSize == self.capacity
    

    ################################################################
    # Retuns parent's index
    # O(c)
    def getParent(self, index):
        return (index-1)/2
    