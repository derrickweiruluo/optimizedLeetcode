"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
  
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

string 理解zigzag的意思, array indexing反转
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # corner cases where res is the input string
        if numRows == 1 or numRows >= len(s):
            return s
        
        
        # this problem is understand the alternating pattern
        # in "row" switching in a string array
        
        res = [""] * numRows
        idx, direction = 0, 1
        
        for char in s:
            res[idx] += char
            if idx == 0:
                direction = 1
            elif idx == numRows - 1:
                direction = -1
            idx += direction
        
        return "".join(res)
