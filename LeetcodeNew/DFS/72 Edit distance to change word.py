'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution1A:   #DFS + MEMO
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(word1, word2, i, j, memo):
            if i == len(word1) and j == len(word2):
                memo[(i, j)] = 0
                return 0
            if i == len(word1):
                memo[(i, j)] = len(word2) - j
                return len(word2) - j
            if j == len(word2):
                memo[(i, j)] = len(word1) - i
                return len(word1) - i
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    res = dfs(word1, word2, i + 1, j + 1, memo)
                else:
                    insert = 1 + dfs(word1, word2, i, j + 1, memo)
                    delete = 1 + dfs(word1, word2, i + 1, j, memo)
                    replace = 1 + dfs(word1, word2, i + 1, j + 1, memo)
                    res = min(insert, delete, replace)
                memo[(i, j)] = res
            return memo[(i, j)]
                
        memo = {}
        
        # do not return memo[(0, 0)] becasue there are early return that not in memo
        # return dfs(word1, word2, 0, 0, memo) 
        dfs(word1, word2, 0, 0, memo) 
        return memo[(0, 0)]


class Solution1B:   #DFS + MEMO
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(word1, word2, i, j): # current idx of i, j in each word
            if i == len(word1) and j == len(word2):
                cache[(i, j)] = 0
                return cache[(i, j)]
            if i == len(word1):
                cache[(i, j)] = len(word2) - j
                return cache[(i, j)]
            if j == len(word2):
                cache[(i, j)] = len(word1) - i
                return cache[(i, j)]
            if (i, j) in cache:
                return cache[(i, j)]
            ## below is when (i, j) not in cache
            if word1[i] == word2[j]:
                res = dfs(word1, word2, i + 1, j + 1)
            else:
                insert = 1 + dfs(word1, word2, i, j + 1)
                delete = 1 + dfs(word1, word2, i + 1, j)
                replace = 1 + dfs(word1, word2, i + 1, j + 1)
                res = min(insert, delete, replace)
            cache[(i, j)] = res
            return cache[(i, j)]
            
        
        cache = {}
        dfs(word1, word2, 0, 0)
        return cache[(0, 0)]