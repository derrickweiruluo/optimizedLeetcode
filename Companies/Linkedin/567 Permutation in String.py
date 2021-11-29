'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False
        
        stringCounter1 = collections.Counter(s1)
        stringCounter2 = collections.Counter()
        
        for i in range(len(s2)):
            stringCounter2[s2[i]] += 1
            if i >= len1:
                if stringCounter2[s2[i - len1]] == 1:
                    del stringCounter2[s2[i - len1]]
                else:
                    stringCounter2[s2[i - len1]] -= 1
            if stringCounter1 == stringCounter2:
                return True
        
        return False