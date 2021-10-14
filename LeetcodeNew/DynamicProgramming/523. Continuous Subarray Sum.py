# prefix sum
"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1

##########
prefix sum, and calculaute the prefix sum remainder of k
if this remainder happended before, and len >= 2: return True
"""

class Solution: # 新代码
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}  # [2,4,9], target == 6, so from idx -1 to idx 1, the len is 2 which satisfy the requirement
        prefixRem = 0
        for idx, num in enumerate(nums):
            prefixRem = (prefixRem + num) % k
            if prefixRem not in seen:
                seen[prefixRem] = idx
            else:
                if idx - seen[prefixRem] > 1:
                    return True
        
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen = {0: -1}  # 最重要的初始化，保证长度 >= 2
        curr_remainder = 0
        
        for idx, val in enumerate(nums):
            curr_remainder = (curr_remainder + val) % k   # prefix_sum of remainder
            if curr_remainder not in seen:
                seen[curr_remainder] = idx
            else:
                # this a step to make sure valid range: len > 2
                # corner cases:
                # if only the first one iteself satisfy, 
                # if the first two together satisfy:     
                if idx - seen[curr_remainder] > 1:      
                    print(idx, seen[curr_remainder])
                    return True
        
        return False
        
        
        

# Explanation:
# cur calculate the prefix sum remainder of input array A
# seen will record the first occurrence of the remainder.
# If we have seen the same remainder before,
# it means the subarray sum if a multiple of k


# Complexity
# Time O(N)
# Space O(N)

    
# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n)
