'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''



'''
Constraints:
s consists only of printable ASCII characters.
'''
class Solution:  # two pointer, best, with early return
    def isPalindrome(self, s: str) -> bool:

        if not s: return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        
        return True



class Solution:  # DONT USE THIS ONE 
    def isPalindrome(self, s: str) -> bool:
        cur = ''
        for i in range(len(s)):
            if s[i].isalnum():
                cur += (s[i].lower())
        print(cur)
        return cur == cur[::-1]