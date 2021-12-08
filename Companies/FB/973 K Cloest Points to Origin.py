

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
        https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)
        https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
        '''
        
        # NlogK Solution
        heap = []
        for x, y in points:
            dist = -1 * (x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [[x, y] for (dist, x, y) in heap]
        
        
        
        # NlogN solution
        return sorted(points, key = lambda x: (x[0] ** 2 + x[1] ** 2))[:k]