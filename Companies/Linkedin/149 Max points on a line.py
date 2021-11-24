'''
给一堆 x, y 坐标点
求最多有几个points 在同一条直线上

'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def inline(a, b, c):
            return (a[1] - b[1]) * (a[0] - c[0]) == (a[1] - c[1]) * (a[0] - b[0])
            
        
        res = 0
        n = len(points)
        if n <= 2: return n
        
        for i in range(n):
            dic = collections.defaultdict(int)
            countSame = 0
            for j in range(i + 1, n):
                if points[j] == points[i]:
                    countSame += 1
                    continue
                flag = 0
                for key in dic:
                    if inline(points[i], points[j], points[key]):
                        dic[key] += 1
                        flag = 1
                        break
                if flag == 0:
                    dic[j] = 1
            curMax = max(dic.values()) if dic else 0
            # curMax = max(list(dic.values()) + [0])
            res = max(res, curMax + countSame + 1)
        return res