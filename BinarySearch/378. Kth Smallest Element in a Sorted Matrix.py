"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

#########
二分模版，比较时候计算当前mid count 有几个小于等于mid的 matrix values
while left < right, converge 出来的就是解

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        left, right = matrix[0][0], matrix[-1][-1]
        m, n = len(matrix), len(matrix[0])
        
        def notGreaterThan(x):
            cnt = 0
            j = n - 1
            for i in range(m):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                cnt += (j + 1)
            return cnt
            
        
        while left < right:
            mid = (left + right) // 2
            if notGreaterThan(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
        
