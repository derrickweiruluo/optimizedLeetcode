"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000

#######
The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return 0
        left, right = 0, nums[0]
        
        count = 1
        while right < len(nums) - 1:
            count += 1
            next_right = max(i + nums[i] for i in range(left, right + 1))
            left, right = left, next_right
        
        return count
