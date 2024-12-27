from graph import Graph


class Maze:
    def __init__(self, width, height):
        self.maze = Graph()

        vertNum = 0
        vertList = []

        # create graph with given dimensions
        for i in range(height):
            for j in range(width):

                currVertex = self.maze.add_vertex(vertNum)
                vertList.append(currVertex)

                # middle/bottom row vertices
                # add edge with above vertex
                if i != 0:
                    aboveVertIndex = len(vertList) - width - 1
                    aboveVert = vertList[aboveVertIndex]
                    self.maze.add_edge(aboveVert, currVertex, 0)

                    # if not leftmost vertex
                    # add edge with left vertex
                    if j != 0:
                        self.maze.add_edge(vertList[j - 1], currVertex, 0)

                vertNum += 1

    # def GenerateDFS(self):





