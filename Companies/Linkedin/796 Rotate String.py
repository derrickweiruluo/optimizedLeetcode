'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

"""
KMP algorithm
time: O(N)
space: O(N)
"""

class Solution: # Leetcode 官方 KMP
    def rotateString(self, A, B):
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False

class Solution:  # discussion KMP
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(A) == 0: return True
        
        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B
        
        # calculate pi table, it captures the length of the
		# longest prefix that is also the suffix
        pi = [0] * (N+1)
        left, pi[0] = -1, -1
        for right in range(1, N+1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left
        
        # do matching
        j = 0
        for i in range(1, (2*N)+1):
            while j >= 0 and B[j+1] != A[i]:
                j = pi[j]
            j += 1
            if j == N: return True
        
        return False

# KMP 算法可以 O(N)
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
class Solution:
    def LPS(self, pattern):
        M = len(pattern)
        lps = [0] * M
        i, j = 1, 0
        while i < M:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps