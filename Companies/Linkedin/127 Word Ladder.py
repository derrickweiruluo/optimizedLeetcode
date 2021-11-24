'''
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
'''


# Time: O(M * M * N), M: length of each word, N: num of words
# Space: O(M * M * N)
# one M for iterate each word, one M for constructing the middle word

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = collections.deque([(beginWord, 1)])
        valid = set(wordList)
        
        while queue:
            cur, length = queue.popleft()
            if cur == endWord:
                return length
            for i in range(len(cur)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = cur[:i] + c + cur[i + 1:]
                    if nextWord in valid:
                        valid.remove(nextWord)
                        queue.append((nextWord, length + 1))
        
        return 0