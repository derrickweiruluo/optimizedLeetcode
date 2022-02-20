'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one

'''


# three windows size==k:w1,w2,w3,can just keep 3 adjacent windows move.
# just like dp,since 3 is small, we can do it manually, update maxw1 if w1>maxw1=> update maxw2 if maxw1+w2>maxw2=>update maxw3 if maxw2+w3>maxw3


# O(N), O(1), sliding window approach
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        win1 = sum(nums[:k])
        win2 = sum(nums[k: 2*k])
        win3 = sum(nums[2*k: 3*k])
        mw1, mw2, mw3 = win1, win1 + win2, win1 + win2 + win3
        
        maxWin1, maxWin2 ,maxWin3 = [0], [0, k], [0, k, 2*k]    #mw1,mw2,mw3's index.
        
        n = len(nums) - 3 * k
        
        for i in range(1, n + 1):#last index for w1 window will be n-3k
            win1 += nums[i-1+k] - nums[i-1]
            win2 += nums[i-1+2*k] - nums[i-1+k]
            win3 += nums[i-1+3*k] - nums[i-1+2*k]
            if win1 > mw1:
                mw1, maxWin1 = win1, [i]
            if mw1 + win2 > mw2:
                mw2, maxWin2 = mw1 + win2, maxWin1 + [i + k]
            if mw2 + win3 > mw3:
                mw3, maxWin3 = mw2 + win3, maxWin2 + [i + 2*k]
        
        
        return maxWin3