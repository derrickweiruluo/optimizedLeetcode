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



## BEST
# O(N + M) & O(1)
class Solution:
    # Approach 3: Start at Top Right, Move Only Left and Down
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        
        # Set pointers to the top-right corner.
        curRow, curCol = 0, cols - 1
        
        # Repeat the search until it goes off the grid.
        while curRow < rows and curCol >= 0:
            if binaryMatrix.get(curRow, curCol) == 1:
                curCol -= 1
            else:
                curRow += 1
        
        # If we never left the last column, it must have been all 0's.
        return curCol + 1 if curCol != cols - 1 else -1


#*-------------------------

# Binary search on each row
# Time:     O(R * log(C))
# SPace:    O(1)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        leftMostCol = cols
        # prev = math.inf
        
        for i in range(rows):
            # set to the previously determined leftMostCol
            left, right = 0, leftMostCol 
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(i, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            leftMostCol = min(leftMostCol, left)
        
        return leftMostCol if leftMostCol < cols else -1


