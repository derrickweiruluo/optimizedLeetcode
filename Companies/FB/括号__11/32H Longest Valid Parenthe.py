'''
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
'''

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.


# Time complexity: O(n). Single traversal of string to fill dp array is done.

# Space complexity: O(n). dp array of size nn is used.

class Solution: #32
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        
        dp = [0] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            
            if stack:
                prev = stack.pop()
                dp[i] = (i - prev + 1) + dp[prev - 1]
                
        return max(dp)