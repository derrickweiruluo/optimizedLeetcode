class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        idx = {0 : -1}
        state, res = 0, 0
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:  #vowels存在当前字母
                state = state ^ 1 << j
            if state not in idx:
                idx[state] = i
            res = max(res, i - idx[state])
        
        return res
