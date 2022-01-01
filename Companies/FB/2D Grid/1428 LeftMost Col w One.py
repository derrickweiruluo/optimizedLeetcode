'''
A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.


You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

1.  BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
2.  BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
'''

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:



# Binary search on each row
# Time:     O(R * log(C))
# SPace:    O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        leftMostCol = cols
        
        for i in range(rows):
            left, right = 0, cols
            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(i, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            leftMostCol = min(leftMostCol, left)
        
        return leftMostCol if leftMostCol < cols else -1