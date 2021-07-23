class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # 这是一个medium if solve in O(logN)
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid
        
        
        return left + k
