# Edge class used for connecting vertices (undirected)
class Edge:
    def __init__(self, fromVert, toVert, weight=1):
        self.fromVert = fromVert
        self.toVert = toVert
        self.weight = weight

