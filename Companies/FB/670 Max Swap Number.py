'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


Constriants: can be no swap
'''

# Python 3 | Greedy, Math | Explanations
# https://leetcode.com/problems/maximum-swap/discuss/846837/Python-3-or-Greedy-Math-or-Explanations
'''Explanation
Basic idea:
Find a index i, where there is a increasing order
On the right side of i, find the max value (max_val) and its index (max_idx)
On the left side of i, find the most left value and its index (left_idx), which is less than max_val
Swap above left_idx and max_idx if necessary
Please check the comments for more detail
Implementation
'''
import collections
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if num < 12: return num
        # nums = list(map(int, str(num)))
        nums = list(str(num))
        n = len(nums)
        
        # step 1: get the first dip and the curMax
        for i in range(n - 1): 
            if nums[i + 1] > nums[i]:
                break
            if i == n - 2:
                return num
        # step 2 store and update the maxIdx and maxVal
        max_val, max_idx = nums[i + 1], i + 1
        for j in range(i + 1, n):
            if nums[j] >= max_val:
                max_val, max_idx = nums[j], j
                
        # step 3 look to the left, get the leftmost smaller than maxVal
        left_idx = i
        for j in range(left_idx, -1, -1):
            if nums[j] < max_val:
                left_idx = j
                
        # Step 4: do the swap
        nums[left_idx], nums[max_idx] = nums[max_idx], nums[left_idx]
        return int(''.join(nums))                           # re-create the integer




class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if num < 12: return num
        
        nums = list(str(num))
        lastSeen = collections.defaultdict(int)
        for i, val in enumerate(nums):
            lastSeen[int(val)] = i
        
        for i, val in enumerate(nums):
            for j in range(9, int(val), -1):
                if lastSeen[j] > i:
                    nums[i], nums[lastSeen[j]] = nums[lastSeen[j]], nums[i]
                    return int("".join(nums))
        
        return num