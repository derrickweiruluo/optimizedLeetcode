'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

'''
mat = [[1,2,3],[4,5,6],[7,8,9]]
        
        pattern
        
             0   1   2
        ----------------    
        0 |  0   1   2
          |          
        1 |  1   2   3
          |          
        2 |  2   3   4w
'''

import collections
class Solution:
    def findDiagonalOrder(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        res = [0] * m * n
        row = col = 0
        d = 1
        
        
        for i in range(m * n):
            res[i] = grid[row][col]
            col += d
            row -= d
            
            # check the upper conditions first, two modification, one dir change
            if row >= m:
                row = m - 1
                col += 2
                d = -d
            if col >= n:
                col = n - 1
                row += 2
                d = -d
            # when below situations happend, only one modification, one dir change
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d

    


        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mapping = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mapping[i + j].append(mat[i][j])
        
        res = []
        for key, lst in mapping.items():
            # 对角线的奇偶规律
            if key % 2 == 0:
                res += lst[::-1]
            else:
                res += lst
        
        return res