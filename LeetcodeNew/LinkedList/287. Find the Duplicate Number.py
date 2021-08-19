"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

 
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3



####################### Like a linkedlist with circle
In this problem, nums[a] = b can be seen as a.next = b, 
the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.

O(n)
"""



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """
        In this problem, nums[a] = b can be seen as a.next = b, 
        the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.
        
        O(n)
        """
        slow, fast = 0, 0
        n = len(nums)
        
        while fast < n and nums[fast] < n:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                
                return slow
        
        
