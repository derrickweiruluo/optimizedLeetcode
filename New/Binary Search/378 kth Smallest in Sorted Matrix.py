'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.




Input: matrix = 
[[1,5, 9],
[10,11,13],
[12,13,15]], 
k = 8

Output: 13
'''

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        left, right = matrix[0][0], matrix[-1][-1]
        m, n = len(matrix), len(matrix[0])
        
        def countLessEqual(x):
            cnt = 0
            j = n - 1       # start with the rightmost column
            for i in range(m):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1      # decrease column until matrix[r][c] <= x
                cnt += (j + 1)
            return cnt
        
        
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1  # try to looking for a smaller value in the left side
            else:
                right = mid     # try to looking for a bigger value in the right side
        
        return left