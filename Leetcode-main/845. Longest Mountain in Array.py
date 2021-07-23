class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        n = len(arr)
        uphill, downhill = [0] * n, [0] * n
        res = 0
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]: 
                uphill[i] = uphill[i - 1] + 1
        
        for i in range(n - 1)[::-1]:
            if arr[i] > arr[i + 1]:
                downhill[i] = downhill[i + 1] + 1
            if uphill[i] > 0 and downhill[i] > 0:
                res = max(res, uphill[i] + downhill[i] + 1)
                
        return res
