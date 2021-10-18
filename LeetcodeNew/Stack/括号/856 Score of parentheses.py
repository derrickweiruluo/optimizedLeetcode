'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

'''

'''
Approach 2: O(1) Space
We count the number of layers.
If we meet '(' layers number l++
else we meet ')' layers number l--
If we meet "()", we know the number of layer outside,

https://leetcode.com/problems/score-of-parentheses/discuss/141777/C%2B%2BJavaPython-O(1)-Space
#笔记本
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
            if char == ')' and s[i - 1] == '(':
                res += 2 ** depth
        return depth

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curVal = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(curVal)
                curVal = 0
            else:
                curVal += stack.pop() + max(curVal, 1)
        
        return curVal