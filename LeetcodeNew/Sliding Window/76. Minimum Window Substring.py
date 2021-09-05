"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = collections.Counter(list(t))
        missing = len(t)
        start = end = 0
        i = 0
        
        for j, char in enumerate(s):
            if target[char] > 0:
                missing -= 1
            target[char] -= 1
            if missing == 0:
                while i < j and target[s[i]] < 0:
                    target[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j + 1
                
                target[s[i]] += 1
                i += 1
                missing += 1
        
        return s[start: end]
        
        
