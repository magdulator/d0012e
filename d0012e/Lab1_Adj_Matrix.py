import random
from heap import Heap

class Graph:
    def __init__(self):
        self.nodes = []     # store all the nodes in a list
        self.nodeSize = 0   # amount of nodes
        self.matrix = []    # the matrix with lists in lists
        self.maxweight = 0
        
    def getGraph(self, amount, maxweight):
        if amount < 2:
            print("Have to be more than 1 nodes")
        else:
            i = 0
            while i < amount:
                self.addNode(i)
                i = i+1
            while self.getConnected() == False:
                randomnumber = random.randint(1, maxweight)
                v1 = random.choice(self.nodes)
                v2 = random.choice(self.nodes)
                if (v1 != v2):
                    self.addEdge(v1, v2, randomnumber)
                
                
    #O(2n+6) 
    def addNode(self, node):
        if node in self.nodes:                  # Cancels nodes that are similar
            print("Node", node, "already exists")
        else:
            self.nodes.append(node)                 # add node to list
            self.nodeSize = self.nodeSize +1        # add 1 to nodesize
            if self.nodeSize > 1:                   #Make the matrix right size and filled with zeros
                for vertex in self.matrix:
                    vertex.append(0)
            temp = []
            for z in range(self.nodeSize):
                temp.append(0)
            self.matrix.append(temp)
        

    #O(7)     
    def addEdge(self, v1, v2, weight):
        if (v1 not in self.nodes):                  # cancels if nodes not exist
            print(v1, "is not an existing node")
        elif (v2 not in self.nodes):
            print(v2, "is not an existing node")
        else:
            pos1 = self.nodes.index(v1)             #place correct wight in the matrix
            pos2 = self.nodes.index(v2)
            self.matrix[pos1][pos2] = weight
            self.matrix[pos2][pos1] = weight
            
    #O(5)     
    def setWeight(self, v1, v2, weight):        # sets weight for a -> b and b -> a to same
        if (weight >= 0):
            pos1 = self.nodes.index(v1)         
            pos2 = self.nodes.index(v2)
            self.matrix[pos1][pos2] = weight
            self.matrix[pos2][pos1] = weight
        else:
            print("Use positive weights")
            

    #O(n+1)            
    def printMatrix(self):                         #print the matrix
        print(self.nodes)
        for i in range(self.nodeSize):
            print(self.nodes[i], self.matrix[i])
            
            
        #0(n^3)
    def primAlgo(self):
        visited = []                    # Visited nodes
        minsum = 0                      # The minimal tree
        visited.append(0)               # Starting index
        best = 0
        
        while range(len(visited)) != range(self.nodeSize):          # Go until all nodes is visited
            minnumber = -1
            for i in visited:                                       # Looks at visited nodes
                for j in range(self.nodeSize):
                    if self.matrix[i][j] > 0 and j not in visited:
                        number = self.matrix[i][j]
                        if minnumber > number or minnumber == -1:   # Choose the best (lowest weight) 
                            minnumber = number
                            best = j
            print(visited)                
            print(minnumber)                
            visited.append(best)                                    # Add the new node to visited
            minsum = minsum + minnumber                             # Add the wheigt
        print(minsum)



    def primAlgoHeap(self):
        Heapvalue = []
        position = []

        for i in range(self.nodeSize):
            for j in range(self.nodeSize):
                heap.insert(heap, self.matrix[i][j])

                print(heap.self.heap)
        
        
    #O(7) + O(5n) + O(2n^2)
    def getConnected(self): 
        connections = []                           # First in first out (list of temp connections)
        connected = [False]*self.nodeSize          # A false graph
        connections.append(0)                      # Start with the first node numbber 0
        i = 0
        while i < len(connections):
            node = connections[i]
            i = i + 1
            if connected[node] == False:
                connected[node] = True
                for j in range(self.nodeSize):      # place new connections in fifo
                    if self.matrix[node][j] > 0 and j not in connections:
                        connections.append(j)

        if len(connections) == self.nodeSize:
            return True
        else:
            return False

g = Graph()
h = Heap(25)



g.getGraph(5,9)
g.getConnected()
g.setWeight(1, 2, 9)
g.printMatrix()
g.primAlgo()
