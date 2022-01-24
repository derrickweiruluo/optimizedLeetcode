'''
数组起初位 1 到 n 的unique postive number, 现在缺少了几个
找到第 k 个 丢失的positive number'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # 这是一个medium if solve in O(logN)
        # from 1 to N (idx 1)
        # k could be greater than N
        
        if k > arr[-1]: return k + len(arr)

        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            
            # arr[mid] is the actual value, (mid + 1) is the position (one-indexed)
            if arr[mid] - (mid + 1) < k:  # not in the left search space(坑位不够 k)
                left = mid + 1
            else:
                right = mid  # in the left search space
        print(left, k)
        return left + k