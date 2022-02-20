'''
Garentee N * N grid


[1,2,3]               [7,4,1]
[4,5,6]  -------->>>. [8,5,2]  
[7,8,9]               [9,6,3]


'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]