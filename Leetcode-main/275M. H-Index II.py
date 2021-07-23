class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #enum = enumerate(citations)
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
            
        return 0
      
#关键在于理解 h index的计算方式：读题
