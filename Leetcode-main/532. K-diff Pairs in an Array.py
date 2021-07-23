class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = collections.Counter(nums)
        res = 0
        
        for num in count:
            if k > 0 and num + k in count or k == 0 and count[num] > 1:
                res += 1
        
        
        return res
