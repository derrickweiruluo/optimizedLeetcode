'''
Give nums
How many subarray products that are less than k

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
'''

# Time O(N), left pointer can only increment N times
# Space O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        i = res = 0
        cur = 1
        for j in range(len(nums)):
            cur *= nums[j]
            while cur >= k:
                cur /= nums[i]
                i += 1
            res += (j - i + 1)
        
        return res