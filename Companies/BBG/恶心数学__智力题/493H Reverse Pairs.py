'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
'''


class Solution:  # Optimal
    def reversePairs(self, nums: List[int]) -> int:

        def ms(l, r):
            if l >= r: return 0
            mid = (l + r) // 2
            count = ms(l, mid) + ms(mid + 1, r)

            j = mid + 1
            for i in range(l, mid+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid - 1

            nums[l:r+1] = sorted(nums[l:r+1])
            return count

        return ms(0, len(nums) - 1)


class Solution:  # BF
    def reversePairs(self, nums: List[int]) -> int:
        
        pos = collections.defaultdict(list)
        
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = 0
        for i, num in enumerate(nums):
            for key, lst in pos.items():
                if num > key * 2:
                    for idx in lst:
                        if idx > i: 
                            res += 1
        
        return res