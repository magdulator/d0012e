class Edge: 
    def __init__(self, node):
        self.node = node
        self.edges = {} # holds nodes it is connected to and weight

    def addConnection(self, neighbor, weight):
        self.edges[neighbor] = weight
 
    def getConnections(self):
        return self.edges.keys()

    def getNode(self):
        return self.node

    def getWeight(self, neighbor):
        return self.edges[neighbor]

    def setWeight(self, neighbor, weight):
        if (weight >= 0):
            self.edges[neighbor] = weight   # sets weight for a -> b and b -> a to same 
            neighbor.edges[self] = weight
        else:
            print("Use positive weights")

class Graph:
    def __init__(self):
        self.edgesDict = {} # list with Edge objects
        self.nodes = []     # store all the nodes in a list
        self.nodeSize = 0   # amount of nodes
        self.matrix = []    # the matrix with lists in lists
        
    def addNode(self, node):
        if node in self.nodes:
            print("Node", node, "already exists")
        newNode = Edge(node)
        self.edgesDict[node] = newNode  #key: 'a', value: Edge object
        self.nodes.append(node)         # add node to list
        self.nodeSize = self.nodeSize +1 # add 1 to nodesize
        if self.nodeSize > 1:           #Make the matrix right size and filled with zeros
            for vertex in self.matrix:
                vertex.append(0)
        temp = []
        for i in range(self.nodeSize):
            temp.append(0)
        self.matrix.append(temp)
        return newNode
            

    def addEdge(self, v1, v2, weight):
        if (v1 not in self.edgesDict):
            print(v1, "is not an existing node")
        elif (v2 not in self.edgesDict):
            print(v2, "is not an existing node")
        else:
            self.edgesDict[v1].addConnection(self.edgesDict[v2], weight)    #two way connection
            self.edgesDict[v2].addConnection(self.edgesDict[v1], weight)
            pos1 = self.nodes.index(v1)                                     #place correct wight in the matrix
            pos2 = self.nodes.index(v2)
            self.matrix[pos1][pos2] = weight
            self.matrix[pos2][pos1] = weight

    def printGraph(self):
        for x in self.edgesDict.values():
            for y in x.getConnections():
                v1 = x.getNode()
                v2 = y.getNode()
                print(v1, v2, x.getWeight(y))

    def printNeighbors(self, v):
        if (v not in self.edgesDict):
            print(v + "is not an exisitng node")

        string = v
        x = self.edgesDict.get(v)
        for y in x.getConnections():
            string = string + str(x.getWeight(y)) + " -> " + str(y.getNode())
        print(string)
                

    def printMatrix(self):                      #print the matrix
        print(self.nodes)
        for i in range(self.nodeSize):
            print(self.nodes[i], self.matrix[i])        

            
g = Graph()
g.addNode('a')
g.addNode('b')
g.addNode('c')
g.addNode('d')
g.addNode('e')

g.addEdge('a', 'b', 1)  
g.addEdge('a', 'c', 2)
g.addEdge('b', 'c', 3)
g.addEdge('a', 'd', 5)
g.addEdge('c', 'b', 4)
g.addEdge('e', 'd', 6)


g.edgesDict['a'].setWeight(g.edgesDict['b'], 20) # set new weight of a->b and b-> a

g.printGraph()

g.printMatrix()
g.printNeighbors('a')

