'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''


# Clarifications:
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.



# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        dp[0][0] = True
        
        for i in range(2, len(p) + 1):
            dp[i][0] = dp[i - 2][0] and p[i - 1] == "*"
        
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == ".")
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]

        return dp[-1][-1]
                    