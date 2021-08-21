"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104




############
O(n) time

"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # partition, left to pivot larger, right smaller
        pos = self.partition(nums)
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 > k:
            return self.findKthLargest(nums[:pos], k)
        else:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
        
        
    def partition(self, nums):
        i, pivot = 0, nums[-1]
        for j in range(len(nums)):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[-1] = nums[-1], nums[i]
        
        return i
