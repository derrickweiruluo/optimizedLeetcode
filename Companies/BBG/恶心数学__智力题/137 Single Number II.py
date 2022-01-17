'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Input: nums = [2,2,3,2]
Output: 3

Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen_once, seen_twice = 0, 0
        
        for num in nums:
            # IF the set "ones" does not have A[i]
            #     Add A[i] to the set "ones" if and only if its not there in set "twos"
            # ELSE
            #     Remove it from the set "ones"
            # change seen_once only if seen_twice is unchanged
            seen_once =  (seen_once ^ num) & (~seen_twice)
            
            
            # IF the set "twos" does not have A[i]
            #    Add A[i] to the set "twos" if and only if its not there in set "ones"
            # ELSE
            #    Remove it from the set "twos"
            # change seen_twice only if seen_once is unchanged
            seen_twice =  (seen_twice ^ num) & (~seen_once)
        
        
        return seen_once