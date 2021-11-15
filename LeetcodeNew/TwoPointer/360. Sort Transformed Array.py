'''
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.


Follow up: Could you solve it in O(n) time?
'''

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [a * x * x + b * x + c for x in nums]
        n = len(nums)
        res = [0] * n
        p1, p2 = 0, n - 1
        
        # i is the start idx of res, delta is the iterating direction
        # this is because a's '-+' can be a totally different graph
        i, delta = (n - 1, -1) if a > 0 else (0, 1)
        while p1 <= p2:
            if nums[p1] * -delta > nums[p2] * -delta:
                res[i] = nums[p1]
                p1 += 1
            else:
                res[i] = nums[p2]
                p2 -= 1
            i += delta
            print(res)
        
        return res