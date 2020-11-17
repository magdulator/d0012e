import random

class Graph:
    def __init__(self):
        self.nodes = []     # store all the nodes in a list
        self.nodeSize = 0   # amount of nodes
        self.matrix = []    # the matrix with lists in lists
        
    def getGraph(self, amount, maxweight):
        if amount < 2:
            print("Have to be more than 1 nodes")
        else:
            i = 0
            while i < amount:
                g.addNode(i)
                i = i+1
            while g.getConnected() == False:
                randomnumber = random.randint(1, maxweight)
                v1 = random.choice(self.nodes)
                v2 = random.choice(self.nodes)
                if (v1 != v2):
                    g.addEdge(v1, v2, randomnumber)
                
                
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
    def printMatrix(self):                      #print the matrix
        print(self.nodes)
        for i in range(self.nodeSize):
            print(self.nodes[i], self.matrix[i])
            
    import random
    
    #O(7) + O(5n) + O(2n^2)
    def getConnected(self): 
        connections = []                           # First in first out (list of temp connections)
        connected = [False]*self.nodeSize   # A false graph
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




g.getGraph(10,9)
g.getConnected()
g.setWeight(1, 2, 9)
g.printMatrix()
