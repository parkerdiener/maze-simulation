from vertex import Vertex
from edge import Edge

# Graph class
# TODO add more header comment


class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertex(self, label):
        # Create and add a new vertex
        vertex = Vertex(label)
        if vertex not in self.edges:
            self.edges[vertex] = []
        return vertex

    def add_edge(self, vert1, vert2, weight):
        edge = Edge(vert1, vert2, weight)
        self.edges[vert1].append(edge)
        self.edges[vert2].append(edge)

    def has_wall(self, vertex_a, vertex_b):
        # Check if an edge exists between two vertices
        for edge in self.edges.get(vertex_a, []):
            if edge.vertex_b == vertex_b and edge.weight == 0:
                return True
        return False
