'''
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}
        
        for i, char in enumerate(s):
            if s[i] in s1 and s1[s[i]] != t[i]:
                return False
            if t[i] in s2 and s2[t[i]] != s[i]:
                return False
            s1[s[i]] = t[i]
            s2[t[i]] = s[i]
            
        return True