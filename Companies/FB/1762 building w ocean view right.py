'''
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''

# contraints:
# 只有smaller，才算有海景

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = collections.deque([n - 1])
        
        for i in range(n - 1, -1, -1):
            if heights[i] > heights[res[0]]:
                res.appendleft(i)
        
        return res