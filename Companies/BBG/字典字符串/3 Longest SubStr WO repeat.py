'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_last_pos = {}
        res = 0
        i = 0
        
        for j, char in enumerate(s):
            if char in char_last_pos:
                # [left, j] has no repeat, [:i] has repeat, thus,
                # if char's last pos + 1 is < left, left stays
                # else, left = char_last_pos[i] + 1
                i = max(i, char_last_pos[char] + 1)
            
            res = max(res, j - i + 1)
            char_last_pos[char] = j
        
        return res