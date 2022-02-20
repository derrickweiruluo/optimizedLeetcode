"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104


Time complexity :O(N) in the average case, O(N^2) in the worst case.
Space complexity : O(1).
"""

class Solution:  # BEST of BEST -- Quick Select w/ random pivot
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        left, right, pos = 0, len(nums) - 1, len(nums)
        while pos + 1 != k:
            pos = self.partition(nums, left, right)
            if pos + 1 < k:
                left = pos + 1
            else:
                right = pos - 1
        return nums[pos]
                
        
    def partition(self, nums, left, right):
        i, p = left, random.randint(left, right)
        pivot_val = nums[p]
        nums[p], nums[right] = nums[right], nums[p]
        for j in range(left, right + 1):
            if nums[j] > pivot_val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i




class Solution:  # NOT 优解，quickselect with random pivot 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/submissions/detail/592804245/
        # partition without random pivot
        
        # https://leetcode.com/submissions/detail/592820805/
        # this one has random partition
        
        pos = self.partition(nums)
        
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 < k:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
        else:
            return self.findKthLargest(nums[:pos], k)
        
    def partition(self, nums):
        # i, pivot = 0, nums[-1]
        i, p = 0, random.randint(0, len(nums) - 1)
        pivot_val = nums[p]
        nums[p], nums[-1] = nums[-1], nums[p]
        for j in range(len(nums) - 1):
            if nums[j] > pivot_val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[-1], nums[i] = nums[i], nums[-1]
        return i   # return the 0-index largest ranking of nums[-1]


# Sample test cases
'''
[6,5,5,4,3,3,2] --> K = 7th largest
if K > required k:
    nums[: K] --> quick select again, same k
else:
    nums[k + 1:] --> quick select again, k = k - K

# 0,1,2,3,4,5,6,7,8
 [3,2,3,1,2,4,5,5,6] --> randinx 2, pivot_val = 3
 [3,2,6,1,2,4,5,5,3] --> swap with the back
 j = 0, i = 0
 j = 1, i = 0
 j = 2, i = 0:  nums[j] <-> nums[i], i ++
 [6,2,3,1,2,4,5,5,3]
 j = 3, i = 1
 j = 4, i = 1
 j = 5, i = 1: nums[j] <-> nums[i], i ++
 [6,4,3,1,2,2,5,5,3]
 j = 6, i =2: nums[j] <-> nums[i], i ++
 [6,4,5,1,2,2,3,5,3]
 j = 7, i =3: nums[j] <-> nums[i], i ++
 [6,4,5,5,2,2,3,1,3]
 j = 8, i = 4is the pivot
 at the end, swap -1, i
 [6,4,5,5,3,2,3,1,2], 比三大的都在左边，且i = 4（0-indexed, 第五大）
 
 
 下一次搜 [6,4,5,5,3]
'''     


# test only for heap solution
class Solution:  # NlogK
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif len(heap) == k:
                heapq.heappushpop(heap, num)
        
        return heap[0]
    
            
