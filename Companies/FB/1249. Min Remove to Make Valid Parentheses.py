'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

'''
class Solution:   # 最优解 O(N), O(1)
    def minRemoveToMakeValid(self, s: str) -> str:
        strArr = list(s)
        n = len(s)
        
        # Step 1 : Iterate from start
        count = 0
        for i in range(n):
            if strArr[i] == '(':
                count += 1
            elif strArr[i] == ')':
                if count == 0:
                    strArr[i] = '#'
                else:
                    count -= 1
        
        # Step 2 : Iterate from end
        count = 0
        for i in range(n - 1, -1, -1):
            if strArr[i] == ')':
                count += 1
            elif strArr[i] == '(':
                if count == 0:
                    strArr[i] = '#'
                else:
                    count -= 1
                    
        # Step 3 : Create "ans" by ignoring the special characters '#'
        res = ""
        for i in range(n):
            if strArr[i] != '#':
                res += (strArr[i])
        
        return res
        return ''.join(char for char in strArr if char != '#')


class Solution:  #Both O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        
        strArr = list(s)
        stack = []
        for i, char in enumerate(strArr):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    strArr[i] = ''
        
        while stack:
            strArr[stack.pop()] = ''
        
        return ''.join(strArr)