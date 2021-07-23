class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = {}
        n = len(s)
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        maxKey = max(counter, key = counter.get) # *****亮点*****
        maxCount = counter[maxKey]
        # print(maxKey)
        if maxCount > (len(s) + 1) // 2:
            return ""
        
        res = [""] * n
        idx = 0
        
        for i in range(maxCount):
            res[idx] = maxKey
            idx += 2
            if idx >= n:
                idx = 1
        del counter[maxKey]
        
        for letter, count in counter.items():
            for i in range(count):
                res[idx] = letter
                idx += 2
                if idx >= n:
                    idx = 1
        
        
        return "".join(res)
