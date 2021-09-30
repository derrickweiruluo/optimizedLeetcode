# Explanation
# dp[index][diff] equals to the length of arithmetic sequence at index with difference diff.

# https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274611/JavaC%2B%2BPython-DP
# Complexity
# Time O(N^2)
# Space O(N^2)


# CASE 1: [9,4,7,2,10]
# dp: 
#    (1, -5): 2, 
#    (2, -2): 2, (2, 3): 2
#    (3, -7): 2, (3, -2): 2, (3, -5): 2
#    (4,  1): 2, (4,  6): 2, (4,  3): 3, (4, 8): 2

# CASE 2: [20,1,15,3,10,5,8]
#    (1, -19): 2, 
#    (2,  -5): 2, (2, 14): 2,
#    (3, -17): 2, (3,  2): 2, (3, -12): 2,
#    (4, -10): 2, (4,  9): 2, (4,  -5): 3, (4,  7): 2,
#    (5, -15): 2, (5,  4): 2, (5, -10): 2, (5,  2): 3, (5,  -5): 4, 
#    (6, -12): 2, (6,  7): 2, (6,  -7): 2, (6,  5): 2, (6,  -2): 2, (6,  3): 2

    
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        # (endIdx, diff) : length
        dp = {}
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1   # length of a new seq is 2, else, curr_len + 1
        
        return max(dp.values())
