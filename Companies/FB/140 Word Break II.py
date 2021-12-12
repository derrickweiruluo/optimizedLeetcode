'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # s = "catcatsanddog" 
            # "cats and dog"
            # "cat sand dog"
        #Output: ["cats and dog",
                #"cat sand dog"]
            
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo) # return list of strings
    
         # 0123456789. @ idx == 10
    # dfs "catcatsand || dog" -> ["cats and dog", "cat sand dog"]
    def dfs(self, s, idx, wordSet, memo):
        if idx == len(s):
            return []
        if s[idx:] in memo:
            return memo[s[idx:]]
        
        res = []
        for word in wordSet:
            if not s[idx:].startswith(word): #substring 不是以这个word开头
                continue
            if s[idx:] == word:
                res.append(s[idx:]) # -> ['dog']
            else:
                restOfResults = self.dfs(s, idx + len(word), wordSet, memo)
                for substring in restOfResults: #当前 dfs的result 非空
                    # 第一个 cat + dfs()
                    # 第二个 cats + dfs()
                    res.append(word + ' ' + substring)
                    
        memo[s[idx:]] = res
        return res