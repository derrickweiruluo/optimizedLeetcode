'''  ALSO ADP PROBLEM
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

 

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

'''

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        
        def dfs(start, end): # [start, end)
            if (start, end) in cache:
                return cache[(start, end)]
            res = 0
            for char in 'abcd':
                left, right = s[start:end].find(char), s[start:end].rfind(char)
                if left != -1 and right != -1:
                    i = start + left
                    j = start + right
                    # i, j will be the one-char palidrome, and then we search its inner part, exclusive
                    res += 2 + dfs(i + 1, j) if i != j else 1
            cache[(start, end)] = res % (10 ** 9 + 7)
            return cache[(start, end)]
        
        cache = {}
        return dfs(0, len(s))
