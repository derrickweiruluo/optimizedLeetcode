'''
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

'''

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        idx1, idx2 = -1, -1
        res = math.inf
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                idx1 = i
                if idx2 >= 0:
                    res = min(res, abs(idx1 - idx2))
            if w == word2:
                idx2 = i
                if idx1 >= 0:
                    res = min(res, abs(idx1 - idx2))
        
        return res