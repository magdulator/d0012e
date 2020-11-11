import random

class Graph:

    def __init__(self, vertices):
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.vertices = vertices
    

    def add_edge(self, v1, v2, weight):
        v1-=1
        v2-=13
        if self.adj_matrix[v1][v2] != 0 or weight < 0:
            return

        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def set_weight(self, v1, v2, weight):
        v1-=1
        v2-=1
        self.adj_matrix[v1][v2] = weight

    def nodes_connected(self, v1, v2):
        if self.adj_matrix[v1][v2] > 0:
            return True
        return False

    def is_connected(self):

        visited = [False] * self.vertices
        count = 0
        for i in range(self.vertices):

            for j in range(self.vertices):

                if not visited[j] and self.adj_matrix[i][j] > 0:
                    visited[j] = True
                    count+=1
        if count == self.vertices:
            return True
        return False

    def print(self):

        for i in range(self.vertices):
            print(self.adj_matrix[i])

def generate_graph(vertices, extra_edges, min_weight, max_weight):
    G = Graph(vertices)

    vertex_count = 1
    for i in range(2,vertices+1):
        vertex = random.randint(1, vertex_count)
        weight = random.randint(min_weight, max_weight)
        #print("Creating edge from ", i, " to ", vertex, " with weight ", weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1

    while extra_edges >= 0:
        src_vertex = random.randint(1, vertices)
        dst_vertex = random.randint(1, vertices)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        extra_edges -= 1

    return G

g = Graph(5)
g.add_edge(1,2,5)
g.add_edge(2,3,5)
g.add_edge(3,4,5)
g.add_edge(4,5,5)

g2 = generate_graph(200, 50, 1, 10)

print(g.is_connected())
