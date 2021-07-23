class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        n = len(wordsDict)
        res = n
        
        p1 = p2 = -1
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                p1 = i
                if p2 >= 0 and p1 != p2:
                    res = min(res, abs(p1- p2))
            
            if word == word2:
                p2 = i
                if p1 >= 0 and p1 != p2:
                    res = min(res, abs(p1 - p2))
                    
        
        return res
        
