"""
1.  We build a list max_range to store the max range it can be watered from each index.
2.  Then it becomes Jump Game II, where we want to find the minimum steps to jump from 0 to n.
3.  The only difference is Jump Game II guarantees we can jump to the last index but this one not. 
    We need to additionally identify the unreachable cases
"""

"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
There are n + 1 taps located at points [0, 1, ..., n] in the garden.
Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
"""


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        dp = [0] * (n + 1)
        for idx, r in enumerate(ranges):
            left, right = max(0, idx - r), min(n, idx + r)
            dp[left] = max(dp[left], right - left)
        
        start, end, steps = 0, 0, 0
        
        while end < n:
            steps += 1
            start, end = end, max(idx + dp[idx] for idx in range(start, end + 1))
            if start == end:   # no movement for "end", thus fail
                return -1
        
        return steps
