# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        leftMostCol = cols
        
        for i in range(rows):
            left, right = 0, cols
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(i, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            leftMostCol = min(leftMostCol, left)
        
        return leftMostCol if leftMostCol < cols else -1
        
        
        # time O(mn)
#         row, col = 0, cols - 1
#         leftMostCol = -1
        
#         while row < rows and col >= 0:
#             if binaryMatrix.get(row, col) == 1:
#                 leftMostCol = col
#                 col -= 1
#             else:
#                 row += 1
        
        
#         return leftMostCol
