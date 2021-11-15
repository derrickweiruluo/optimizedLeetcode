'''
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.


Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        # sort() --> null 
        # return sorted([a * x * x + b * x + c for x in nums])  # O(NlogN)
        # merge sort + bucket sort
        # input nums is pre-sorted

        nums = [a * x * x + b * x + c for x in nums]
        # if a < 0, input nums[-1] == 0: return nums

        n = len(nums)
        res = [0] * n
        p1, p2 = 0, n - 1
        idx, delta = (0, 1) if a < 0 else (n - 1, -1)  # for direction depending on a
        while p1 <= p2:
            l , r = nums[p1], nums[p2]
            if a >= 0:
                if l > r:
                    res[idx] = l
                    p1 += 1
                else:
                    res[idx] = r
                    p2 -=1
                idx -= 1    # when a >= 0. idx start from n - 1
            else: # a < 0
                if l > r:
                    res[idx] = r
                    p2 -= 1
                else:
                    res[idx] = l
                    p1 += 1
                idx += 1    # when a < 0. idx start from 0
        
        return res # non-decreasing