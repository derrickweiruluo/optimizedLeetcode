'''
给你一个sorted 外星人 的 String Array
return 他们的 alpha order (Char order)

'''


class Solution:
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
                # 从不相同的字符, update dict, 然后结束
                if ch1 != ch2:
                    par[ch2].add(ch1)
                    child[ch1].add(ch2)
                    break
        

        # Step 2: topological sort with deque
        res = []
        queue = collections.deque()
        
        list_no_par_node = [i for i in par if len(par[i]) == 0]
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