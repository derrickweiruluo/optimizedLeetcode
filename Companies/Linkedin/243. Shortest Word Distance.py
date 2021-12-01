class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        i = j = -1
        res = math.inf
        for idx in range(len(wordsDict)):
            if wordsDict[idx] == word1:
                i = idx
                if j >= 0:
                    res = min(res, abs(i - j))
            if wordsDict[idx] == word2:
                j = idx
                if i >= 0:
                    res = min(res, abs(i - j))
        
        return res