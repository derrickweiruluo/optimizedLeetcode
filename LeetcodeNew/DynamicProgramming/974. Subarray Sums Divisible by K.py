class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        res = 0
        
        # The biggest trick is tracking the occurrence of each possible remainder
        # for rem = 0, it start from 1 (count)
        # for all other rem, start from 0
        
        rem_count = [0] * k
        rem_count[0] = 1
        cur_rem = 0
        
        for num in nums:
            cur_rem = (cur_rem + num) % k
            res += rem_count[cur_rem]
            rem_count[cur_rem] += 1
        
        return res
