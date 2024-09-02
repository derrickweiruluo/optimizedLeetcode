import heapq
import collections
from typing import List


class Solution_heapq:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)
        print(counter)
        heap = [(-count, key) for key, count in counter.items()]
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


class Solution_sort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        sorted_counter = dict(
            sorted(counter.items(), key=lambda item: item[1], reverse=True)
        )
        res = []
        for key in sorted_counter.keys():
            res.append(key)
            if len(res) == k:
                return res
        return res
