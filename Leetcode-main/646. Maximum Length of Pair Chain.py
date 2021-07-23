class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        sortedPairs = sorted(pairs, key = lambda x: x[1])
        
        currRight, res = -math.inf, 0
        
        for pair in sortedPairs:
            if pair[0] > currRight:
                currRight = pair[1]
                res += 1
        
        return res
