class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix #计算每一行从index 1到n 的sum
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]

    def update(self, row: int, col: int, val: int) -> None:
        row = self.matrix[row]
        diff = val - (row[col] - (row[col-1] if col else 0)) #diff 等于 （现值-边界的sum差）
        for i in range(col, len(row)):
            row[i] += diff # update 从col开始到尾部的sum with diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            res += self.matrix[i][col2] - (self.matrix[i][col1-1] if col1 else 0)
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
