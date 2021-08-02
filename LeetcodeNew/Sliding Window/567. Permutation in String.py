"""
Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.
 
##. Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

##  Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
##. Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        s1_count = collections.Counter(s1)
        window_count = collections.Counter()
        
        for i in range(len2):
            window_count[s2[i]] += 1
            if i >= len1:
                if window_count[s2[i - len1]] == 1:
                    del window_count[s2[i - len1]]
                else:
                    window_count[s2[i - len1]] -= 1
            # if i == 4:
            #     print(window_count, s1_count)
            if window_count == s1_count:
                return True
        
        return False
