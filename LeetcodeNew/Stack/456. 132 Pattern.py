'''
Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

https://leetcode.com/problems/132-pattern/discuss/206575/previous-greater-element-(-stack-O(n)-no-reverse)
https://leetcode.com/problems/132-pattern/


stack is (cur_min, mid), where left < mid (ALWAYS)
keep adding to stack(cur_min, mid), popping to meet the first condition, until met
then check if cur_num > the current smallest


'''


import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        smallest = math.inf
        stack = []
        
        for i in range(len(nums)):
            while stack and stack[-1][1] <= nums[i]:    # (a, b) where b <= c,  
                stack.pop()                             # until b > c met
            if stack and stack[-1][0] < nums[i]:        # (a, b) where a < c met as well
                return True
            stack.append((smallest, nums[i]))
            smallest = min(smallest, nums[i])
        
        return False