'''
类 C/c++ 的 String 转 Integer Atoi function

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

'''

# https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        s = list(s.strip()) # 除掉space，转换inpu，t以及sanity check
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1  # 确定 sign
        if s[0] in '-+':
            del s[0]

        res = i = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + ord(s[i]) - ord('0')  # get the num
            i += 1
        
        return max(- 2** 31, min(sign * res, 2 ** 31 - 1))