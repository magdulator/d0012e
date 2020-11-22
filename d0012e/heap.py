import math

class Heap:
    ################################################################
    # Heap constructor
    def __init__(self):
        self.heap = []            #Heap List
        self.Edgelist = []        #List of corresponding edges
        self.currentSize = 0      #Current size of heap list
        self.weightlist = []
        self.minsum = 0

    
    ################################################################
    # Inserts weight and corresponding edge
    # cost: O(c)
    
    def insert(self, weight, edge):
        self.heap.append(weight)
        self.Edgelist.append(edge)
        self.fixHeap(self.currentSize)
        self.currentSize += 1


    ################################################################
    # sorts the list 
    # cost: O(n)
    def fixHeap(self, index):
        if self.currentSize == 0:
            return
        
        newValue = self.heap[index]
        newEdge = self.Edgelist[index]

        while (index > 0 and newValue < self.heap[self.getParent(index)]):
            parentIndex = self.getParent(index)
            self.heap[index] = self.heap[parentIndex]
            self.Edgelist[index] = self.Edgelist[parentIndex]
            index = self.getParent(index)
        
        self.heap[index] = newValue
        self.Edgelist[index] = newEdge


    
    ################################################################
    # Returns root of heaplist and fix list
    # cost: O(c)


    def extractMin(self):
        
        if self.currentSize == 0:           #Dont go if heap is empty
            return

        root = self.Edgelist[0]

        self.minsum = self.minsum + self.heap[0]    # Increase the minsum

        last = self.heap[self.currentSize - 1]      # Change place with the last node
        self.heap[0] = last

        lastEdge = self.Edgelist[self.currentSize - 1]  # Change place with last Edge
        self.Edgelist[0] = lastEdge
        
        del self.Edgelist[self.currentSize - 1]         # Delete last node and Edge
        del self.heap[self.currentSize - 1]

        self.currentSize -= 1
        self.minHeapify(0)                              # Now place first element in heap on the right place

        return root



    #########################################################################
    # Sorts the list but from the other direction from top to bot
    # cost: O(n)

    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.currentSize and self.heap[left] < self.heap[smallest]:       # Look at first Child
            smallest = left 
  
        if right < self.currentSize and self.heap[right] < self.heap[smallest]:     # Look at second Child
            smallest = right

        if smallest != idx:                                                         # Change with the smallest Child if the child is smaller then itself

            small = self.Edgelist[smallest]                                         # Switch in Edgelist
            big = self.Edgelist[idx]        
            self.Edgelist[idx] = small
            self.Edgelist[smallest] = big
            
            small = self.heap[smallest]                                             # Switch in heap
            big = self.heap[idx]        
            self.heap[idx] = small
            self.heap[smallest] = big

            self.minHeapify(smallest)                                               # Do it again untill it has find its place in heap
            
        
    ################################################################
    # Retuns parent's index
    # cost: O(c)
    def getParent(self, index):
        return int((index-1)/2)

    def print(self):
        for i in range(self.currentSize):
            print (self.hea[i], self.Edgelist[i])

