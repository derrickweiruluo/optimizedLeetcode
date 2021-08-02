"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        anagram_len = len(p)
        res = []
        
        p_count = collections.Counter(p)
        s_count = collections.Counter()
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= anagram_len:   # sliding window
                if s_count[s[i - anagram_len]] == 1:
                    del s_count[s[i - anagram_len]]    # 减到0就要删除，不然下一步比较不出来
                else:
                    s_count[s[i - anagram_len]] -= 1   # count -= 1 for exisiting key:count

            if s_count == p_count:   # compare curr window to target
                res.append(i - anagram_len + 1)
        
        return res
                    
        
        
