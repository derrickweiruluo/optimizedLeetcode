'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character



EXAMPLE:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

'''For both the memoized and dynamic programming solutions, the runtime is O(mn) and the space complexity is O(mn) where m and n are the lengths of word1 and word2, respectively.'''


# Both O(mn)
class Solution:
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


class Solution4:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]


'''
Of course, an interative implementation is usually better than its recursive counterpart because we don't risk blowing up our stack in case the number of recursive calls is very deep. We can also use a 2D array to do essentially the same thing as the dictionary of cached values. When we do this, we build up solutions from smaller subproblems to bigger subproblems (bottom-up). In this case, since we are no longer "recurring" in the traditional sense, we initialize our 2D table with base constraints. The first row and column of the table has known values since if one string is empty, we simply add the length of the non-empty string since that is the minimum number of edits necessary to arrive at equivalent strings. For both the memoized and dynamic programming solutions, the runtime is O(mn) and the space complexity is O(mn) where m and n are the lengths of word1 and word2, respectively.'''

class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]