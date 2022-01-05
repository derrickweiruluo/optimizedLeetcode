'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
'''

class Solution:  # 20ms  interview
    # DFS + Memo 
    # time: O(N^2 to 2^N), 和解的数量有关
    # time: roughly O(N^3)
    # space O(2^N) --> worst case
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo)
    
    def dfs(self, s, idx, wordSet, memo):
        if s[idx:] in memo:
            return memo[s[idx:]]
        if idx == len(s):
            return [""]
        
        res = []
        for word in wordSet:
            # 保证左半部分合理
            if not s[idx:].startswith(word):
                continue
            if s[idx:] == word:
                res.append(word)
            else:
                # 递归求解右半部分
                restOfTheResults = self.dfs(s, idx + len(word), wordSet, memo)
                for item in restOfTheResults:
                    if item:
                        res.append(word + ' ' + item)
        
        memo[s[idx:]] = res
        return res

        # s = "catcatsanddog" 
            # "cats and dog"
            # "cat sand dog"
        #Output: ["cats and dog","cat sand dog"]



# Consider the input "aaaaaa", with wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"]. Every possible partition is a valid sentence, and there are 2^n-1 such partitions. It should be clear that the algorithm cannot do better than this since it generates all valid sentences. The cost of iterating over cached results will be exponential, as every possible partition will be cached, resulting in the same runtime as regular backtracking. Likewise, the space complexity will also be O(2^n) for the same reason - every partition is stored in memory.

# Where this algorithm improves on regular backtracking is in a case like this: "aaaaab", with wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"], i.e. the worst case scenario for Word Break I, where no partition is valid due to the last letter 'b'. In this case there are no cached results, and the runtime improves from O(2^n) to O(n^2).


class Solution: # this is huahua's shorter codes
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(s, wordSet):
            if s in memo:
                return memo[s]
            
            res = []
            if s in wordSet:
                res.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right in wordSet:
                    res += [word + " " + right for word in dfs(s[0:i], wordSet)]
            
            memo[s] = res
            return memo[s]
        
        return dfs(s, wordSet)




# ---------------------------------------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
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