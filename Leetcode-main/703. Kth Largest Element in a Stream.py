# https://docs.python.org/3/library/heapq.html
# 经典heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            # automatically maintain the heap invariant
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            # automatically maintain the heap invariant
            heapq.heapreplace(self.minHeap, val)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
