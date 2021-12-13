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
        
        s = list(str(num))
        n = len(s)
        for i in range(n - 1):                                # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i + 1]: break
            if i == n - 2:
                return num                                    # if nothing find, return num
                                     
        max_idx, max_val = i+1, s[i + 1]                      # keep going right, find the maximum value index
        for j in range(i + 1, n):
            if max_val <= s[j]: 
                max_idx, max_val = j, s[j]
        left_idx = i                                        # going right from i, find most left value that is less than max_val
        for j in range(i, -1, -1):    
            if s[j] < max_val: 
                left_idx = j
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]   # swap maximum after i and most left less than max
        return int(''.join(s))                              # re-create the integer




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