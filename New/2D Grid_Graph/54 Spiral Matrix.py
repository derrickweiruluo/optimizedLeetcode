'''

1 2 3
4 5 6
7 8 9

--> [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return res
        up, down = 0, m - 1
        left, right = 0, n - 1
        while len(res) < n * m:
            # 每一圈: 
            # row from left to right, right to left
            # col from top + 1 to bottom - 1, bottom - 1 to top + 1

            for j in range(left, right + 1, 1):
                if len(res) < n * m:
                    res.append(matrix[up][j])
            for i in range(up + 1, down, 1):
                if len(res) < n * m:
                    res.append(matrix[i][right])
            for j in range(right, left - 1, -1):
                if len(res) < n * m:
                    res.append(matrix[down][j])
            for i in range(down - 1, up, -1):
                if len(res) < n * m:
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            down -= 1
            up += 1
        
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