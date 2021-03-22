class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i,row in enumerate(self.rectangle):
            if i >= row1 and i <= row2:
                for j in range(len(row)):
                    if j >= col1 and j <= col2:
                        self.rectangle[i][j] = newValue
        return None

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]