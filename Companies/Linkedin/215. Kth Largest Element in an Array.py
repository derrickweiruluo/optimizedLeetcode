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


Time complexity :O(N) in the average case, O(N^2) in the worst case.
Space complexity : O(1).
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """the partition function is 0-index based partition, thus all
        comparision in the recursive call is between pos + 1 vs k, where k
        is 1-indexed
        
        !!!! Each partion call will rearrange the nums   !!!!
        """
        pos = self.partition(nums)
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 > k:
            return self.findKthLargest(nums[:pos], k)
        else:
            return self.findKthLargest(nums[pos + 1:], k - (pos + 1))

    # partition function return a 0-index based K-largest position
    def partition(self, nums):
        """put all larget than pivot, nums[-1], to the front, every partition,
        i += 1, upon checking all values in nums, i is at the position where
        the pivot should go, then swap nums[i] and nums[-1]
        the return i is a 0-index largest position"""
        
        i, pivot = 0, nums[-1]
        for j in range(len(nums)):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[-1] = nums[-1], nums[i]
        
        return i  # return the 0-index largest ranking of nums[-1]
        
    
            
