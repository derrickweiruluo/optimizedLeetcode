'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
'''


'''
    1.  Integers in each row are sorted from left to right.
    2.  The first integer of each row is greater than the last integer of the previous row.

    matrix = 
    [1, 3, 5, 7]
    [10,11,16,20]
    [23,30,34,60]

target = 3
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n, m = len(matrix), len(matrix[0])
        
        left, right = 0, n * m - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // m][mid % m] < target:
                left = mid + 1
            else:
                right = mid
        
        return matrix[left // m][left % m] == target