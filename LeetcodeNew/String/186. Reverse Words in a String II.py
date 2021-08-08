"""
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.
 

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
 

##################
Constraints:
##################
1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.

"""

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # a reverse method works for char or string
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        # print(s)
        left = 0
        reverse(0, len(s) - 1)              # reverse all char first
        # print(s)
        
        for idx, char in enumerate(s):      # then reverse "no-space word as char"
            if char == " ":     
                reverse(left, idx - 1)      # idx - 1 is the curr right bound
                left = idx + 1              # idx + 1 is the next left bound
        
        reverse(left, len(s) - 1)           # reverse the last word 
