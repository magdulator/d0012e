
class Graph:
    def __init__(self):
        self.nodes = []     # store all the nodes in a list
        self.nodeSize = 0   # amount of nodes
        self.matrix = []    # the matrix with lists in lists
        

    #O(2n+6) 
    def addNode(self, node):
        if node in self.nodes:                  # Cancels nodes that are similar
            print("Node", node, "already exists")
            return()
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




g.setWeight('a','b', 9)
g.printMatrix()
