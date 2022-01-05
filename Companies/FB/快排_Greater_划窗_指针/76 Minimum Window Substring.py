'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 用counter来确认包含所有元素
        counter = collections.Counter(t)
        l = len(t)
        missing = l

        start, end = 0, 0
        i = 0
        for j, char in enumerate(s):
            if counter[char] > 0:
                missing -= 1
            counter[char] -= 1
            if missing == 0:
                while i < j and counter[s[i]] < 0:  # <0 意味着有多余的可以缩left bound
                    counter[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start - 1:
                    start, end = i, j + 1
                    
                counter[s[i]] += 1
                missing += 1
                i += 1
        
        return s[start: end]