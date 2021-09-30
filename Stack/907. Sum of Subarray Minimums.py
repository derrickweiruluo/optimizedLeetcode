"""
I use a monotonous non-decreasing stack to store the left boundary and right boundary where a number is the minimal number in the sub-array

e.g. given [3,1,2,4],
For 3, the boudary is: | 3 | ...
For 1, the boudray is: | 3 1 2 4 |
For 2, the boudray is: ... | 2 4 |
For 4, the boudary is: ... | 4 |

The times a number n occurs in the minimums is |left_bounday-indexof(n)| * |right_bounday-indexof(n)|
The total sum is sum([n * |left_bounday - indexof(n)| * |right_bounday - indexof(n)| for n in array])
After a number n pops out from an increasing stack, the current stack top is n's left_boundary, the number forcing n to pop is n's right_boundary.
A tricky here is to add MIN_VALUE at the head and end.
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        res = 0
        stack = [] # non-decreasing stack
        nums = [-1] + arr + [-1]
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                cur = stack.pop()
                res += nums[cur] * (idx - cur) * (cur - stack[-1])
                print(res)
            
            stack.append(idx)
        
        return res % (10 ** 9 + 7)
