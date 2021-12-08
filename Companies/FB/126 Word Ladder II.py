'''

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

'''

import collections, string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        validWords = set(wordList)
        res = []
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        lowercase = string.ascii_lowercase
        
        while layer:
            newLayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    for lst in layer[w]:
                        res.append(lst)
                else:
                    for i in range(len(w)):
                        for char in lowercase:
                            newWord = w[:i] + char + w[i + 1:]
                            if newWord in validWords:
                                for lst in layer[w]:
                                    newLayer[newWord].append(lst + [newWord])
            
            validWords -= set(newLayer.keys())
            layer = newLayer
            
        return res
        