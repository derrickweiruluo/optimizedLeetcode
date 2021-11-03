"""
把word1 转换成 word2， 在given wordlist范围内一个字母一个字母改变来完成转换，返回最短改变次数，如果不行，返回0

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

####
time:   O(M2 * N) where MM is the length of each word and NN is the total number of words in the input word list.
space:  O(M2 * N)

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # 当前word，每个index，尝试改变有且仅有一个字母， 如果转换后的在wordlist
                    # 从wordlist中删除，然后加到queue的尾巴
                    # 第一个word的双循环找完以后，queue剩下的就是转换一次后的候选人
                    # 然后以此类推BFS， 每一层都 length + 1
                    nextWord = word[:i] + char + word[i + 1:]
                    if nextWord in wordList:
                        wordList.remove(nextWord)  # to prevent 重复查找
                        queue.append([nextWord, length + 1])
        
        return 0
