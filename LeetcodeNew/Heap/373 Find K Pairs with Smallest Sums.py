'''
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

'''
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        m, n = len(nums1), len(nums2)
        res = []
        visited = set()
        
        # 每个iteration heappop一个解，且把下两个最小的push 进 heap
        # heap of (small, idx_i, idx_j)
        for _ in range(min(k, m * n)):
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return res