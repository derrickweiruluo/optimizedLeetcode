'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix: return 0
        
        m, n = len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        
        for i in range(m):
            
            # Calcualte the "row-wise" height based on the previous row
            # if at prev row and current index j, height[j] == 0, then curr row and col == 0
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            stack = [-1]
            
            # Using stack to scan left to make sure it is a valid rectangle
            for j in range(n + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - 1 - stack[-1]
                    res = max(res, h * w)
                
                stack.append(j)
        
        
        return res