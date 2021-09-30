'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Ex1:
Input: s = "bcabc"
Output: "abc"

Ex2:
Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last_idx = {}  # {char: last_appeared_idx}
        res = []
        
        for i, char in enumerate(s):
            last_idx[char] = i
            
        for i, char in enumerate(s):
            # 第一次的char出现，再出现 & 因为大小关系被pop掉了，就不在res，再加入，假如被保留了，那就skip掉
            
            if char not in res:     
                # res[-1] is a char that has an index MUST < than current idx
                # cond1: res 非空
                # cond2: 当前char 比 res[-1] 小
                # cond3: 且res[-1] 对应的 char 后面还有重复的
                
                while res and char < res[-1] and last_idx[res[-1]] > i:
                    res.pop()
                res.append(char)
        
        return ''.join(res)