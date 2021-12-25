'''array of strictly increasing integers
All positive, increasing,: unique, 1-index

'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # 这是一个medium if solve in O(logN)
        # from 1 to N (idx 1)
        # k could be greater than N
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid
        
        print(left, k)
        return left + k