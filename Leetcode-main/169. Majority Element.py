class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # *** One liner NlogN Solution ***
        # return sorted(nums)[len(nums) // 2] 
        
        
        count = 0
        candidate = math.inf
        
        
        # *** Boyer-Moore Voting Algorithm *** 
        for num in nums:
            if count == 0:
                candidate = num
                
            count += 1 if num == candidate else - 1
            
        return candidate
