'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        while matrix: # 2D matrix 调转
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
            
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        length = m * n
        
        res = []
        while matrix: # 2D matrix 调转
            res.extend(matrix.pop(0))
            # matrix = [*zip(*matrix)][::-1]
            if len(res) == length:
                break
            n = len(matrix[0])
            matrix = [[row[i] for row in matrix] for i in range(n - 1, -1, -1)]
            
        return res
