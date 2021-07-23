# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
#         counter = {}
        
#         for char in s:
#             if char not in counter:
#                 counter[char] = 1
#             else:
#                 counter[char] += 1

        counter = collections.Counter(s)
        
        res = 0
        bigOdd = 0
        
        for char, count in counter.items():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                bigOdd = 1
                
        
        return res + bigOdd
