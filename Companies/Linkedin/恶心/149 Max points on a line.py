'''
给一堆 x, y 坐标点
求最多有几个points 在同一条直线上

'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        if n <= 2: return n
        
        def inline(a, b, c):
            # (a[1] - b[1]) / (a[0] - b[0]) == (a[1] - c[1]) / (a[0] - c[0])
            # to avoid divide zero
            return (a[1] - b[1]) * (a[0] - c[0]) == (a[1] - c[1]) * (a[0] - b[0])
        
        res = 0
        for i in range(n):
            memo = collections.defaultdict(int)
            countDuplicate = 0
            for j in range(i + 1, n):
                if points[j] == points[i]:
                    countDuplicate += 1
                    continue
                flag = 0
                for key in memo:
                    if inline(points[key], points[i], points[j]):
                        memo[key] += 1
                        flag = 1
                        break
                if flag == 0:
                    memo[j] = 1
            
            curMax = max(memo.values()) if memo else 0
            res = max(res, curMax + countDuplicate + 1)
            print(not memo, curMax + countDuplicate + 1)
        
        return res