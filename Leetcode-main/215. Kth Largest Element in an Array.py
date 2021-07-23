# Classic Quick Select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while True:
            pos = self.partition(nums, left, right)
            print(nums)
            print(left, right, "res is: ", pos)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 < k:
                left = pos + 1
            else:
                right = pos - 1
                
                
    def partition(self, nums, left, right):
        randomidx = random.randint(left, right)
        pivot = nums[randomidx]
        nums[left], nums[randomidx] = nums[randomidx], nums[left]
        
        i, j = left + 1, right
        
        while i <= j:
            if nums[i] < pivot < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
            if nums[i] >= pivot: i += 1
            if nums[j] <= pivot: j -= 1
        
        nums[j], nums[left] = nums[left], nums[j]
        return j
                


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104
