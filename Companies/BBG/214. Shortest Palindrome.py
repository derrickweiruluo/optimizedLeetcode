# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.


class Solution:  #KMP, both O(N)
    def shortestPalindrome(self, s: str) -> str:
        
        cur = s + '|' + s[::-1]
        lps = [-1] + [0] * len(cur)
        left, right = -1, 0
        
        while right < len(cur):
            while left >= 0 and cur[left] != cur[right]:
                left = lps[left]
            left += 1
            right += 1
            lps[right] = left
                
        return s[lps[-1]:][::-1] + s
        

class Solution:  # Brute Force O(N2)
    def shortestPalindrome(self, s: str) -> str:
        
        re = s[::-1]
        i = len(s)
        
        while not s[:i] == re[len(s) - i:]:
            i -= 1
        
        return re[:len(s) - i] + s