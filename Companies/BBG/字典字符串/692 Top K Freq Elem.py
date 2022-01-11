'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Input: nums = [1], k = 1
Output: [1]
'''

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