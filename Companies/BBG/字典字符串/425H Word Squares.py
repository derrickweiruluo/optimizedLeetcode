'''
Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).



Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''


# Append next prefix if row[i] == col[i] in arr
class Solution:
    def wordSquares(self, words):
        pref, res = collections.defaultdict(set), []
        for w in words:
            for i in range(len(w)):
                pref[w[:i + 1]].add(w)
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                for w in pref["".join(row[i] for row in arr)]:
                    dfs(i + 1, arr + [w])   
        for w in words:
            dfs(1, [w])
        return res


def wordSquares(self, words):
    n = len(words[0])
    memo = collections.defaultdict(list)
    for word in words:
        for i in range(n):
            memo[word[:i]].append(word)
    def build(square):
        if len(square) == n:
            squares.append(square)
            return
        for word in memo[''.join(zip(*square)[len(square)])]:
            build(square + [word])
    squares = []
    for word in words:
        build([word])
    return squares