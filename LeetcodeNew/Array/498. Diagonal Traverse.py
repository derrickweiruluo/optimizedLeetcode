"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        """
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        
        pattern
        
             0   1   2
        ----------------    
        0 |  0   1   2
          |          
        1 |  1   2   3
          |          
        2 |  2   3   4
                
        """
        mapping = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mapping[i + j].append(mat[i][j])
        
        res = []
        for key, lst in mapping.items():
            if key % 2 == 0:
                res += lst[::-1]
            else:
                res += lst
        
        return res
