"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
 
Constraints:

0 <= num <= 108
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if num < 12: return num
        
        nums = list(str(num))
        last = {int(val): idx for idx, val in enumerate(nums)}
        
        for i, val in enumerate(nums):
            for d in range(9, int(val), -1):
                if last.get(d, 0) > i:
                    nums[i], nums[last[d]] = nums[last[d]], nums[i]
                    return int("".join(nums))
        
        
        return num
