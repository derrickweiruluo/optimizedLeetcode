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



"""
If we know source and destination, 
we can build the word tree by going forward in one direction and backwards in the other. 
We stop when we have found that a word in the next level of BFS is in the other level, 
but first we need to update the tree for the words in the current level.
Then we build the result by doing a DFS on the tree constructed by the BFS.
The difference between normal and double BFS is that the search changes 

"""

# time reduced from O(k^d) to O(k^(d/2) + k^(d/2)). 
# 
class Solution:  # bi-BFS
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, front, back, nextLayer, rev = False, {beginWord}, {endWord}, set(), False
        while front and not found:
            words -= set(front)
            for x in front:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in string.ascii_lowercase]:
                    if y in words:
                        if y in back: 
                            found = True
                        else: 
                            nextLayer.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            front, nextLayer = nextLayer, set()
            if len(front) > len(back): 
                front, back, rev = back, front, not rev
        def backtrack(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in backtrack(y)]
        return backtrack(beginWord)






class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        from collections import defaultdict
        dict = set(dict)
        #将end添加进dict,防止结果为[]
        dict.add(end)
        res = []
        # 记录单词下一步能转到的单词
        next_word_dict = defaultdict(list)
        # 记录到start距离
        distance = {}
        distance[start] = 0
        
        # 暴力匹配,当前字符串修改一个字母后的新字符串存在于dict中
        def next_word(word):
            ans = []
            for i in range(len(word)):
                       #97=ord('a')，123=ord('z')+1  
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in dict:
                        ans.append(tmp)
            return ans
        # 求到start的距离
        def bfs():
            q = collections.deque()
            q.append(start)
            step = 0
            flag = False #标记是否找到结果
            while len(q) is not 0:
                step += 1
                n=len(q)
                for i in range(n):
                    word=q[0]
                    q.popleft()
                    for nextword in next_word(word):
                        next_word_dict[word].append(nextword)
                       #当下一跳是end时，就可以结束搜索
                        if nextword == end:
                            flag = True
                        #如果没被添加过，则进行添加
                        if nextword not in distance:
                            distance[nextword] = step
                            q.append(nextword)
                if flag:
                    break
        # 遍历所有从start到end的路径
        def dfs(tmp, step):
            if tmp[-1] == end:
                res.append(tmp)
                return
            for word in next_word_dict[tmp[-1]]:
                if distance[word] == step + 1:
                    dfs(tmp + [word], step + 1)
        #bfs搜start--end的最短路径