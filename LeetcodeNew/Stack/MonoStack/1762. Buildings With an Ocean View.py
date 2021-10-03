'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''
import collections
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        res = collections.deque([len(heights) - 1])
        for i in range(len(heights) - 1)[::-1]:
            if heights[i] > heights[res[0]]:
                res.appendleft(i)
        
        print(res)
        return res