'''84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
https://leetcode.com/problems/largest-rectangle-in-histogram/

test

'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0

        # must have this step, always 从idx + 1 扫描 idx -- stopped idx 的长度
        # mono-increasing stack of height
        heights = heights + [0]  
        stack = []

        # which enables swipe from right to left with "fixed height", == heights[stack.pop()]
        # popping the stack until stopped, width == nextIdx - stack[-1]
        # 具体细节 width 和 height 需要手解， 每次popping都有可能产生最优解
        # EX：  [1,2,3,4,5,6] + [0], 
        #       areas: 6 * 1, 5 * 2, 4 * 3, etc        
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                res = max(res, h * w)
                # print(i, h, w, i, stack[-1] if stack else '#')
            stack.append(i)
        
        return res