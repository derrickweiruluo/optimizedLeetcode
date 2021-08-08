"""
1.  We build a list max_range to store the max range it can be watered from each index.
2.  Then it becomes Jump Game II, where we want to find the minimum steps to jump from 0 to n.
3.  The only difference is Jump Game II guarantees we can jump to the last index but this one not. 
    We need to additionally identify the unreachable cases
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
