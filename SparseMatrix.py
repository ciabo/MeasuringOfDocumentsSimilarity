class SparseMatrix:
    def __init__(self):
        self.matrix = {}

    def addValue(self, rowIndex, columnIndex):
        if rowIndex in self.matrix:
            self.matrix[rowIndex].append(columnIndex)
        else:
            list = [columnIndex]
            self.matrix[rowIndex] = list

    def addValueWithCheck(self, rowIndex, columnIndex):  # add the columnIndex only if it is not already present in the list
        if rowIndex in self.matrix:
            if columnIndex not in self.matrix[rowIndex]:  # check if the columnIndex is not already in the list...
                self.matrix[rowIndex].append(columnIndex)
        else:
            list = [columnIndex]
            self.matrix[rowIndex] = list

    def isEmpty(self, rowIndex):
        if rowIndex not in self.matrix:
            return True
        else:
            return False

    def getColumns(self, rowIndex):
        return self.matrix[rowIndex]

    def getKeys(self):
        return list(self.matrix.keys())
