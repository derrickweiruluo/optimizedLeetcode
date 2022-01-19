'''
Given an array of strings words, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).
'''

# 要求 k 行 k 列读出来的word都一样，且for every k (kth row)


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            for j in range(len(word)):
                # word 太长
                if j >= len(words):
                    return False
                # word 太短
                if len(words[j]) <= i:
                    return False
                # different char
                if words[i][j] != words[j][i]:
                    return False
        
        return True