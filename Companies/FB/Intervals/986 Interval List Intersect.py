'''
给两个 intervals lists, A, B

return 他们所有的交集， empty的交集也算，例如[22,22]
'''


# Clarifications:
# All of them are closed intervals
# interval is valid from length of zero, inclusing zero, [22,22]


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        m, n = len(A), len(B)
        i = j = 0
        res = []
        
        while i < m and j < n:
            # common working time
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            
            if low <= high:
                res.append([low, high])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        
        return res







class Solution:  # BAD BAD BAD BAD BAD BAD BAD Early code
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        m, n = len(firstList), len(secondList)
        res = []
        
        
        while i < m and j < n:
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            if a_start <= b_end and b_start <= a_end:  # Cross-section area
                res.append([max(a_start, b_start), min(a_end, b_end)])  # get the overlapping
            
            # Next step is regardless, advance i or j based on the end time value
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        
        return res