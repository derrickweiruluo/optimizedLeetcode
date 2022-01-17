'''
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

'''

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        validWords = set(wordList)
        res = []
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        lowercase = string.ascii_lowercase
        
        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    for lst in layer[word]:
                        res.append(lst)
                else:
                    for i in range(len(word)):
                        for char in lowercase:
                            newWord = word[:i] + char + word[i + 1:]
                            if newWord in validWords:
                                for lst in layer[word]:
                                    newLayer[newWord].append(lst + [newWord])
            
            validWords -= set(newLayer.keys())
            layer = newLayer
            
        return res