'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
'''




'''
All the above approaches have ignored a key piece of information in the problem statement:

1. The integers in the input array arr satisfy 1 ≤ arr[i] ≤ n, where n is the size of array.

2. This presents us with two key insights:

All the integers present in the array are positive. i.e. arr[i] > 0 for any valid index i.
The decrement of any integers present in the array must be an accessible index in the array.
i.e. for any integer x in the array, x-1 is a valid index, and thus, arr[x-1] is a valid reference to an element in the array.

the next time we see an element x, we don't need to negate again! If the value at index abs(x)-1 is already negative, we know that we've seen element x before.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            
            nums[abs(num) - 1] *= -1
        
        
        return res