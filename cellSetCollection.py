# cellSetCollection class for implementing different maze algorithms
# Map that has each cell correspond to a set of connected cells

class cellSetCollection:

    def __init__(self, allCells):

        self.cellDict = {}

        # initialize by mapping each cell to a set that only contains itself
        for cell in allCells:
            cellSet = set()
            cellSet.add(cell)
            self.cellDict[cell] = cellSet

    # Returns set of given cell
    def getSet(self, cell):
        return self.cellDict[cell]

    # Merge two of the sets
    def merge(self, cellSet1, cellSet2):

        mergedSet = set(cellSet1)
        mergedSet.update(cellSet2)

        for cell in mergedSet:
            self.cellDict[cell] = mergedSet
