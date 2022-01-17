'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
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