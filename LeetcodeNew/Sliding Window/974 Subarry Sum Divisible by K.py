

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counter = collections.Counter()
        counter[0] = 1
        res = prefixRem = 0
        
        for i, num in enumerate(nums):
            prefixRem = (prefixRem + num) % k
            res += counter[prefixRem]
            counter[prefixRem] += 1
        
        return res