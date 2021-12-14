'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''



'''
Follow-ups:
Q1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
A1: Compare half of 1 row with half of the next/previous row.

Q2. What if the matrix is so large that you can only load up a partial row into the memory at once?
A2 :Hash 2 rows (so only 1 element needs to be loaded at a time) and compare the results, excluding the appropriate beginning or ending element.
A2: need two file pointer, the first one start at [0][0], the second one starts at [1][1], load two elements each time, compare and move

'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        
        return True
        
        