'''
https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)
https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
https://leetcode.com/submissions/detail/611702872/
'''

# Quick Select, O(N), O(H), Worst case O(N^2), O(H) for n * n-1 * n-2...
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(cord):
            return cord[0] ** 2 + cord[1] ** 2
        
        def partition(left, right):
            randPivot = randint(left, right)
            points[right], points[randPivot], = points[randPivot], points[right]
            i, pivotDist = left, dist(points[right])
            for j in range(left, right + 1):  # skip the last index, do the last swap after the for loop
                if dist(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            # points[-1], points[i] = points[i], points[-1]
            return i - 1 # return numbers of val <= than pivot_dist
        
        left, right, pos = 0, len(points) - 1, len(points)
        while pos != k:
            pos = partition(left, right)
            # print(pos, points)
            if pos < k:
                left = pos + 1
            else:
                right = pos - 1
        
        return points[:k]
        
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = -1 * (x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        
        return [[x, y] for dist, x, y in heap]