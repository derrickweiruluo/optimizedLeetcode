class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
      # Med 高频 amazon ms， 496变种，circular list and stack 基操
        stack = []
        res = [-1] * len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
            
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
                
        return res
