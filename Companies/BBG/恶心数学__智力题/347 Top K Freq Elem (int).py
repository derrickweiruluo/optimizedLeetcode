class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # It is guaranteed that the answer is unique.
        # which means, no conflict if there is tie
        
        # bucket sort: https://leetcode.com/submissions/detail/602987983/
        
        counter = collections.Counter(nums)
        buckets = collections.defaultdict(list)
        maxFreq = 0
        
        for num, freq in counter.items():
            buckets[freq].append(num)
            maxFreq = max(maxFreq, freq)
        
        res = []
        for freq in range(maxFreq, -1, -1):
            if freq in buckets:
                res += buckets[freq]
            if len(res) == k:
                return res


###### Heap nlogn 解  NOT THE BEST
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res   





#######
class solution:
    def topKFrequent(self, nums, k):
        freq = collections.defaultdict(list)
        for key, cnt in collections.Counter(nums).items():
            freq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(freq[times])
            if len(res) >= k: return res[:k]

        return res[:k]