'''
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

Ex1:
Input: s = "aacaba"
Output: 2    ("aac", "aba"),  ("aaca", "ba")

EX2:
Input: s = "abcd"
Output: 1    ("ab", "cd")

EX3:
Input: s = "aaaaa"
Output: 4
'''

class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        leftCnt = collections.Counter()     # left window start with ''
        rightCnt = collections.Counter(s)   # right window start with the original string
        
        for i in range(len(s)):
            # at every idx, Add/Substract the left/right counter, check the len
            leftCnt[s[i]] += 1
            rightCnt[s[i]] -= 1
            if rightCnt[s[i]] == 0: # since right only decrease in count, if 0, delete the key
                del rightCnt[s[i]]
            if len(leftCnt) == len(rightCnt):
                print(i)
                res += 1
        
        return res