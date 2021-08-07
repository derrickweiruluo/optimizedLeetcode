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
        
        res = len(s) + 1
        missing = len(t)
        
        target = collections.Counter(list(t))
        start, end = 0, 0
        left = 0
        
        for right, char in enumerate(s, 1):  # right start from 1
            if target[char] > 0:
                missing -= 1
            target[char] -= 1
            if missing == 0:
                while left < right and target[s[left]] < 0:
                    target[s[left]] += 1
                    left += 1
                target[s[left]] += 1
                missing += 1
                if end == 0 or right - left < end - start:
                    start, end = left, right
                
                left += 1
        
        return s[start: end]
        
        
