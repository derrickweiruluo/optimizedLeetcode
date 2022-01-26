'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
'''


# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.


'''
find next greater in a circular array
'''


# Loop once, we can get the Next Greater Number of a normal array.
# Loop twice, we can get the Next Greater Number of a circular array

# Input: nums = [1,2,3,4,3] -> [2,3,4,-1,4] 
# input:  [1,  2, 3, 4, 3]

# Stack is a stack of indexes
# res =   [-1,-1,-1,-1,-1],   stack; [3,4]
# 1st:    [2,  3  4 -1,-1],   stack: [3,3,4]
# 2nd:    [2,  3, 4,-1, 4] 

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        stack = []
        
        for i in range(2 * n - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        
        
        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = [] # increasing stack of nums idx
        res = [-1] * len(nums)
        
        for i in range(len(nums)): # first loop tp get next greater in normal array
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
            
        for i in range(len(nums)): # second loop tp get next greater in circular array. for those idx could not find next greater
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        
        return res