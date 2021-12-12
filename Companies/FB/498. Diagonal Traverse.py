'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        res = [0] * m * n
        
        row = col = 0
        d = 1
        
        for i in range(m * n):
            # print(i)
            res[i] = mat[row][col]
            row -= d
            col += d
            
            if row >= m:
                row = m - 1
                col += 2
                d = -d
            if col >= n:
                col = n - 1
                row += 2
                d = -d
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d
        
        return res