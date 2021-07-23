class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # part1: build the child, parent relationship for each char is comparable
        child = {}
        par = {}
        
        for word in words:
            for char in word:
                child[char] = set()
                par[char] = set()
        
        for word1, word2 in zip(words[:-1], words[1:]):
            # check if word1 include word2, which is a invalid case
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    par[ch2].add(ch1)
                    child[ch1].add(ch2)
                    break
        
        # part2: topological sort with deque
        res = []
        queue = collections.deque()
        
        list_no_par_node = [i for i in par if len(par[i]) == 0]
        
        for node in list_no_par_node:
            del par[node]
            queue.append(node)
        
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
                    
        if par:
            return ""
        return "".join(res)
