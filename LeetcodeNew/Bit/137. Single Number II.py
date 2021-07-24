
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen_once, seen_twice = 0, 0
        
        for num in nums:
            # change seen_once only if seen_twice is unchanged
            seen_once =  (seen_once ^ num) & (~seen_twice)
            
            # change seen_twice only if seen_once is unchanged
            seen_twice =  (seen_twice ^ num) & (~seen_once)
        
        
        return seen_once
