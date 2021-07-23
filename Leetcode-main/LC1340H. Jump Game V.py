class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[i] > arr[j]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
