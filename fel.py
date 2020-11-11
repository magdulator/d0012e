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


class Graph():
    def __init__(self):
        self.edgesDict = {} # list with Edge objects
        self.nodes = []  #store all the nodes
        self.nodeSize = 0
        self.matrix = []
        
    def addNode(self, node):
        if node in self.nodes:
            print("nodes", node, "already exist")
        else:
            self.nodes.append(node)
            self.nodeSize = self.nodeSize +1
            if self.nodeSize > 1:
                for vertex in self.matrix:
                    vertex.append(0)
            temp = []
            for i in range(self.nodeSize):
                temp.append(0)
            self.matrix.append(temp) 
 #       newNode = Edge(node)
  #      self.edgesDict[node] = newNode  #key: 'a', value: Edge object
   #     return newNode

    def addEdge(self, v1, v2, weight):
        if (v1 not in self.edgesDict):
            print(v1, "is not an existing node")
        elif (v2 not in self.edgesDict):
            print(v2, "is not an existing node")
        else:
            self.edgesDict[v1].addConnection(self.edgesDict[v2], weight)    #two way connection
            self.edgesDict[v2].addConnection(self.edgesDict[v1], weight)
            index1 = self.matrix(v1) 
            index2 = self.matrix(v2)
            self.matrix[index1][index2] = e

    def printGraph(self):
        for x in self.edgesDict.values():
            for y in x.getConnections():
                v1 = x.getNode()
                v2 = y.getNode()
                print(v1, v2, x.getWeight(y))

    def printMatrix(self):
        for i in range(self.nodeSize):
            for j in range(self.nodeSize):
                if self.matrix[i][j] !=0:
                    print([i][j])            

g = Graph()
g.addNode("a")
g.addNode("b")
g.addNode("c")
g.addNode("d")

g.addEdge("a", "b", 1)  
g.addEdge("a", "c", 2)
g.addEdge("a", "d", 3)
g.addEdge("b", "c", 5)

#g.edgesDict['a'].setWeight(g.edgesDict['b'], 20) # set new weight of a->b and b-> a

g.printGraph()

g.printMatrix()
