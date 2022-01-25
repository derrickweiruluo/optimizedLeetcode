'''
给你一个sorted 外星人 的 String Array
return 他们的 alpha order (Char order)

'''


######  解释 和 拓扑排序
"""
Topological Sort Based Solution
Synoposis
    The basic idea behind this problem is simple. Build a graph from the dictionary of words. 
    Then do a topological sort of the words. The meat is in the details and corner cases.
Meaning of Lexicographically Smaller
    Understanding what lexicographically smaller really means. 
    Notice that adjacent words in the dictionary dictate the order. 
    Letters within the word do not determine the lexicographic order. 
    https://discuss.leetcode.com/topic/22395/the-description-is-wrong
Building an Input Graph
    - Graph is a dictionary with key as character and edge end points as a set
    - Every adjacent pair of word is extracted. All their characters are added to a graph as keys
    - Now every adjacent character is compared. The first non-matching character determines a relationship u -> v and is added to graph. 
      We break at this point since the remainder mis-matches do not imply any relationship.
    - Notice a pair like ("wrtkj","wrt") - > this indicates no relationship since wrt match 
      and then the smaller word is actually longer length than bigger word. 
      This needs to be reported as an error.
    - build_graph method returns the graph. If an error is found, empty graph is returned.
Topological Sort
    DFS or BFS can be used to implement topological sort. We use DFS.
    We run topological sort on each vertex.
    Topological sort requires a directed acyclic graph. If there is a cycle, we return True.
    How do we detect a cycle? We use the concept of back-edges. We maintain a visiting and visited array.
    Topological sort can be implemented using BFS as well. https://www.youtube.com/watch?v=71eHuQvSwc0
"""
"""
Interesting Examples
["wrtkj","wrt"] # Incorrect input
["a","b","a"] # Cycle
["wnlb"]
"""

import collections

# 拓扑要求： 
# 1. DAG(directed acyclic graph)
# 2. 每个 v只出现一次

#### 小当家
class Solution:  # topological sorting
    def alienOrder(self, words) -> str:
        chars = set("".join(words))
        graph = collections.defaultdict(set)
        indegree = {char: 0 for char in chars}
        for i, word1 in enumerate(words[:-1]):
            word2 = words[i + 1]
            if len(word1) > len(word2) and word2 == word1[:len(word2)]:
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                if c2 not in graph[c1]:
                    indegree[c2] += 1
                graph[c1].add(c2)
                break

        
        res = ''
        queue = collections.deque([char for char in indegree if not indegree[char]])
        while queue:
            char = queue.popleft()
            res += char
            for nei in graph[char]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    queue.append(nei)
        return res if len(res) == len(indegree) else ''




class Solution:  # 写法1，后面的 topo不够好
    def alienOrder(self, words: List[str]) -> str:

        # Step 1: build the child, parent relationship for each char is comparable
        # O (NK)
        child = {}
        par = {}
        
        for word in words:
            for char in word:
                child[char] = set()
                par[char] = set()
        
        for word1, word2 in zip(words[:-1], words[1:]):
            # check if word1 include word2, which is a invalid order
            # check if word1 is in word2 in the first len(word1)
            if word1[:len(word2)] == word2 and len(word1) > len(word2):
                return ""
            
            for ch1, ch2 in zip(word1, word2):
                # 第一个不相同的字符, update dict, 然后 break
                if ch1 != ch2:
                    par[ch2].add(ch1)
                    child[ch1].add(ch2)
                    break
        

        # Step 2: topological sort with deque
        res = []
        queue = collections.deque()
        
        list_no_par_node = [i for i in par if len(par[i]) == 0]
        if not list_no_par_node:
            return ""
        # 因为 大小是通过比较不同的word来得到的
        # 假如 char 只存在一个 word，那就是没比较
        # 所以返回的顺序无所谓
        # ["zy","zx"] --> zyx or yxz, since z, y only appears in word1
        
        for node in list_no_par_node:
            del par[node]
            queue.append(node)
        
        # if there is circle in the dict, queue does not constructed fully
        while queue:
            node = queue.popleft()
            res.append(node)
            children = child[node]
            for ch in children:
                par[ch].remove(node)
                # only proceed to add the child node if the child node has no parent
                if len(par[ch]) == 0:
                    queue.append(ch)
                    del par[ch]
                    
        if par: # has circle
            return ""

        return "".join(res)


# Your input
# ["z","x","a","zb","zx"]

# Before
# {'z': {'a'}, 'x': {'z', 'b'}, 'a': {'x'}, 'b': set()}
# {'z': {'x'}, 'x': {'a'}, 'a': {'z'}, 'b': {'x'}}

# After, if there is circle in the dict, queue does not constructed fully
# deque(['b'])
# {'z': {'a'}, 'x': {'z'}, 'a': {'x'}}


