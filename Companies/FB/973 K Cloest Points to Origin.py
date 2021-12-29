

''' Clarification
You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq


# Heap solution
# O(NlogK) for time, O(k) space for heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
        https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)
        https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
        '''
        
        # O(NlogK) Time and O(K) Space Solution
        heap = []
        for x, y in points:
            heapVal = -1 * (x ** 2 + y ** 2)
            if len(heap) == k:
                heapq.heappushpop(heap, (heapVal, x, y))
            else:
                heapq.heappush(heap, (heapVal, x, y))
        
        return [[x, y] for val, x, y in heap]
        
        
        
        # NlogN solution
        return sorted(points, key = lambda x: (x[0] ** 2 + x[1] ** 2))[:k]