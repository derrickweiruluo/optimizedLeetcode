"""
Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3

"""

class Solution:  # O(1)
    def minAddToMakeValid(self, s: str) -> int:
        left_add = 0
        right_add = 0
        for char in s:
            if char == "(":
                right_add += 1
            elif char == ")":
                if right_add:
                    right_add -= 1
                else:
                    left_add += 1
        return left_add + right_add
                


class Solution_ON:
    def minAddToMakeValid(self, s: str) -> int:
        lefts = "("
        stack = []
        matching = {"(": ")"}
        count = 0

        for char in s:
            if char in lefts:
                stack.append(char)
            else:
                if not stack or matching[stack.pop()] != char:
                    count += 1
        return count + len(stack)
