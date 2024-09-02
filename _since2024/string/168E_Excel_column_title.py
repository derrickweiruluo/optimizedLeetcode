"""
Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        distance = ord("A")
        while columnNumber > 0:
            y = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            res = chr(y + distance) + res
        return res
