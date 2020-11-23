import random
import time
import math
from heap import Heap
class Edge: 
    def __init__(self, node):
        self.node = node
        self.edges = {} # holds nodes it is connected to and weight

    def addConnection(self, neighbor, weight): # O(1)
        self.edges[neighbor] = weight
 
    def getConnections(self): #O(1)
        return self.edges.keys()

    def getNeigbours(self):
        return self.edges

    def getNode(self): # O(1)
        return self.node

    def getWeight(self, neighbor): # O(1)
        return self.edges[neighbor]

    def setWeight(self, neighbor, weight): #O(2)
        if (weight >= 0):
            self.edges[neighbor] = weight   # sets weight for a -> b and b -> a to same 
            neighbor.edges[self] = weight
        else:
            print("Use positive weights")

    



class Graph:
    def __init__(self):
        self.edgesDict = {} # list with Edge objects

    def addNode(self, node): # O(3)
        newNode = Edge(node)
        self.edgesDict[node] = newNode  #key: 'a', value: Edge object {'a': {'c':1, 'd':1}, 'c':{'a':1}, 'd':{'a':1}}
        return newNode

    def addEdge(self, v1, v2, weight): # O(5) + O(1) + O(1)
        if (v1 not in self.edgesDict):
            print(v1, "is not an existing node")
        elif (v2 not in self.edgesDict):
            print(v2, "is not an existing node")
        else:
            self.edgesDict[v1].addConnection(self.edgesDict[v2], weight)    #two way connection
            self.edgesDict[v2].addConnection(self.edgesDict[v1], weight)

    def setWeight(self, v1, v2, weight):
        if (v1 not in self.edgesDict):
            print(v1, "is not an existing node")
        elif (v2 not in self.edgesDict):
            print(v2, "is not an existing node")
        else:
            self.edgesDict[v1].setWeight(self.edgesDict[v2], 20)
    
    #O(8) + O(n) + O(2n^2)
    def connectivity(self):
        nodesList = [] #All current nodes in tree
        connectedList = [] #Connected nodes in tree
        nodesList = list(self.edgesDict.keys())
        connectedList.append(nodesList[0])

        for v in connectedList:     #loop through connected nodes, start at index 0
            x = self.edgesDict.get(v)
            for y in x.getConnections():                #loop through nodes connections
                if y.getNode() not in connectedList:    
                    connectedList.append(y.getNode())   #add the neighbor of node to connectedList

        if len(connectedList) >= len(nodesList):        #all nodes are connected
            return True
        else:
            return False

            
    def printGraph(self): #O(3n^2)
        for x in self.edgesDict.values():
            for y in x.getConnections():
                v1 = x.getNode()
                v2 = y.getNode()
                print(v1, v2, x.getWeight(y))

    def printNeighbors(self, v): #O(n+4)
        if (v not in self.edgesDict):
            print(v + "is not an exisitng node")
        else:
            string = v
            x = self.edgesDict.get(v)
            for y in x.getConnections():
                string = string + " Weight: " + str(x.getWeight(y)) + " -> Node: " + str(y.getNode()) + " "
            print(string)

    def makeGraph(self, nodeAmount, maxWeight):
        if nodeAmount < 2:
           print("Need to have atleast 2 nodes")
        else:
            for i in range(nodeAmount+1):
                self.addNode(str(i))
            
            while self.connectivity() == False:
                n1 = self.edgesDict[str(random.randint(0, nodeAmount))]
                n2 = self.edgesDict[str(random.randint(0, nodeAmount))]
                if n1 != n2:
                    if n2.getNode() not in n1.getConnections():
                        self.addEdge(n1.getNode(), n2.getNode(), random.randint(1, maxWeight))

    # O(N^2 + E)
    def primAlgo(self, startNode):
        start_time = time.time()
        visited = [startNode]           #add all visited nodes to list 
        totalCost = 0
        chosenNode = 0
        while range(len(visited)) != range(len(self.edgesDict)): 
            minWeight = -1
            for key in visited:         # looks att all nodes that has been visited for smallest edge
                neighbours = self.edgesDict.get(key).getNeigbours().items()     # {objekt: weight}
                for neighbour in neighbours:                                  
                    if neighbour[0].getNode() not in visited:                   #index 0 = object holding node, index 1 = weight
                        if neighbour[1] < minWeight or minWeight == -1:      #looks at all the neighbour weights for node to get minimum
                            minWeight = neighbour[1]
                            chosenNode = neighbour[0].getNode()
            visited.append(chosenNode) 
            totalCost += minWeight

        print("Total weight without heap: " + str(totalCost))
        #print ("Time for prim without heap: ", time.time() - start_time)

    # O(E+N)*log(N))
    def primAlgoHeap(self):
        start_time = time.time()
        minHeap = Heap()
        size = len(self.edgesDict)
        
        for i in range(size):                                  # Place the amount of nodes in in heap
            minHeap.insert(math.inf, i)
        minHeap.heap[0] = 0

        while len(minHeap.heap) > 0:                                          # Go untill heap is empty 
            heapnode = minHeap.extractMin()                                   # Take away the first (smallest) int in the list and replace it with the second smallest
            neighbours = self.edgesDict.get(str(heapnode)).getNeigbours().items()
            for neighbour in neighbours:                                
                neighbourNode = int(neighbour[0].getNode())                  #loop through all neighbours

                if neighbourNode in minHeap.nodeList:                        # If it is still in nodeList WHICH ARE NODES
                    index = minHeap.nodeList.index(neighbourNode)
                    if neighbour[1] < minHeap.heap[index]:                   # If the weight is lower than some other choise same node has replace the weight with the smaller    
                        minHeap.heap[index] = neighbour[1]          
                        minHeap.fixHeap(index)                      
                            
            minHeap.minHeapify(0)                                             # Look at the first element in list and make sure its the lowest
        print("minimum weight is:", minHeap.minsum)
        #print ("Time for prim with heap: ", time.time() - start_time)


g = Graph()

g.makeGraph(100, 10)

#g.printGraph()

g.primAlgo('0')
#g.primHeap()

g.primAlgoHeap()
##g.addNode('a')
##g.addNode('b')
##g.addNode('c')
##g.addNode('j')
##
##g.addEdge('a', 'b', 1)  
##g.addEdge('a', 'c', 2)
##g.addEdge('b', 'c', 3)
##g.addEdge('j', 'q', 5)
##
##g.setWeight('a', 'b', 20) # set new weight of a->b and b-> a
##
##g.printGraph()
##g.printNeighbors('a')


