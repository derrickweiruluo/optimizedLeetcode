# 127 Word Ladder


# Bi directionary BFS
# https://leetcode.com/problems/word-ladder/discuss/40710/Share-my-two-Python-solutions%3A-a-very-concise-one-(12-lines-~160ms)-and-an-optimized-solution(~100ms)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        validWords = set(wordList)
        lowercase = string.ascii_lowercase

        if endWord not in validWords: return 0
        dist = 1
        front, back = {beginWord}, {endWord}

        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in lowercase:
                        if c != word[i]:
                            nextWord = word[:i] + c + word[i + 1:]
                            if nextWord in back:
                                return dist
                            if nextWord in validWords:
                                next_front.add(nextWord)
                                validWords.remove(nextWord)
            
            front = next_front
            if len(back) < len(front):
                front, back = back, front
    
        return 0


# 单向BFS 暴力版
import collections, string
from math import dist
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = collections.deque([(beginWord, 1)])
        validWords = set(wordList)
        lowercase = string.ascii_lowercase
        # lowercase = 'abcdefghijklmnopqrstuvwxyz'
        
        while queue:
            cur, length = queue.popleft()
            if cur == endWord:
                return length
            for i in range(len(cur)):
                for char in lowercase:
                    nextWord = cur[:i] + char + cur[i + 1:]
                    if nextWord in validWords:
                        validWords.remove(nextWord)
                        queue.append((nextWord, length + 1))
        
        
        return 0



