''' Clarification
You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(cord):
            return cord[0] ** 2 + cord[1] ** 2
        
        def partition(nums, left, right):
            randPivot = randint(left, right)
            nums[right], nums[randPivot] = nums[randPivot], nums[right]
            i, pivotDist = left, dist(nums[right])
            for j in range(left, right + 1):
                if dist(nums[j]) <= pivotDist:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            return i - 1 # return numbers of val <= than pivot_dist
        
        left, right, pos = 0, len(points) - 1, len(points)
        while pos != k:
            pos = partition(points, left, right)
            if pos < k:
                left = pos + 1
            else:
                right = pos - 1
        
        return points[:k]




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