'''
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

#######

https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC%2B%2BPython-Priority-Queue
Complexity
Time O(NlogK)
Space O(K)


'''

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        Explanation
        Heap heap store k height difference that we need to use ladders.
        Each move, if the height difference d > 0,
        we push d into the priority queue pq.
        If the size of queue exceed ladders,
        it means we have to use bricks for one move.
        Then we pop out the smallest difference, and reduce bricks.
        If bricks < 0, we can't make this move, then we return current index i.
        If we can reach the last building, we return A.length - 1.

        '''
        
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        
        return len(heights) - 1
            
