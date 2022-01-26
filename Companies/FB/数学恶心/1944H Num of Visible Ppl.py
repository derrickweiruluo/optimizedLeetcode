'''
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).


Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
'''

# contraints:
# n == heights.length
# 1 <= n <= 105
# All the values of heights are unique.
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] >= heights[stack[-1]]:
                res[i] += 1
                
                # each pop(), cur ppl seen += 1, and will be invisible for
                # the next ppl on the left, which also maintain mono
                stack.pop()
            if stack:
                res[i] += 1
            # print(i, stack)
            stack.append(i)
        
        return res

# similar next greater
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359868/JavaPython-3-Monotonic-increasing-stack-w-18-similar-problems-brief-explanation-and-analysis.