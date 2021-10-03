'''1130. Minimum Cost Tree From Leaf Values
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

input: [6,2,4]
output: 32: == 8 + 24 == sum(maxLeftLeave * maxRightLeave)

  24
 /  \
6    8
    /  \
   2    4


https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space
'''
import math
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # [6,2,4,13,15,10,8,9,5,4,3,2]
        # [6,2,4,7]
        
        res = 0
        stack = [math.inf]  # non-increasing stack
        for i in range(len(arr)):
            while stack[-1] <= arr[i]:
                mid = stack.pop()
                res += mid * min(stack[-1], arr[i])  # construct and summing non-leaf nodes, next-greater 
            stack.append(arr[i])
        
        for i in range(2, len(stack)):              # construct and summing left over non-leaf nodes
            res += stack[i - 1] * stack[i]
        
        return res