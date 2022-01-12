'''
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

# Assumption, garantee there is an answer
# Ask for O(1) Space and Linear Time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = math.inf
        
        
        # *** Boyer-Moore Voting Algorithm *** 
        for num in nums:
            if count == 0:
                candidate = num
                
            count += 1 if num == candidate else - 1
            
        return candidate