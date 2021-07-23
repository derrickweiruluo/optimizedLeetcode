class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        wordSet = set(wordDict)
        
        dp = [False for i in range(n + 1)]
        dp[0] = True # It is always true if start the word start from left end
        
        for i in range(1, n + 1):
            for word in wordSet:
                if dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True
                    
        return dp[-1]
