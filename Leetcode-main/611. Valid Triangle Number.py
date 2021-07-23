class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        sortedNums = sorted(nums)
        res = 0
        
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if sortedNums[left] + sortedNums[right] > sortedNums[i]:
                    # 下面这一步是算都duplicate combination, 符合条件就右 -= 1
                    res += (right - left)
                    right -= 1
                else:
                    # 不行的话就 左 += 1
                    left += 1
        
        # time O(n^2), one for loop in while loop
        return res
