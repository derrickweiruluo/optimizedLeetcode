'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
'''
import collections
# https://www.youtube.com/watch?v=M_PzYd59_kk

# Monotonic queue: stores unique values of dp[i - k + 1 : i] in DESC order

class Solution:  # Huahua, MUCH efficient
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = collections.deque([0])  # deque of idx in nums
        
        for i in range(1, n):
            dp[i] = nums[i] + dp[queue[0]]
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop() # keep desc order in queue
            while queue and i - queue[0] >= k:
                queue.popleft()  # maintain a sliding window of size k
            queue.append(i)
        
        return dp[n - 1]



class Solution: # early solution 05/2021
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = collections.deque()
        queue.append(0)
        
        for i in range (1, n):
            while queue and queue[0] + k < i:
                queue.popleft()
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        return dp[-1]