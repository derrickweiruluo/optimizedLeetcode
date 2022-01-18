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




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                res = max(res, i - start + 1)
                
            used[c] = i

        
        return res