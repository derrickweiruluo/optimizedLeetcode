'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Ex 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Ex 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Ex 3:
Input: haystack = "", needle = ""
Output: 0
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        l = len(needle)
        if not l:
            return 0
        
        for i in range(0, len(haystack) - l + 1):
            if haystack[i: i + l] == needle:
                return i
        
        return -1