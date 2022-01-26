'''
在一个 2D grid 里面给一堆坐标


求最大 reactangle 面积， 长方形可以是斜着的
'''


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        seen = collections.defaultdict(list)
        res = math.inf
        
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                centerX = (x1 + x2) / 2
                centerY = (y1 + y2) / 2
                diagonal = (x1 - x2) ** 2 + (y1 - y2) ** 2
                for xx, yy in seen[(centerX, centerY, diagonal)]:
                    area = sqrt(((x1 - xx) ** 2 + (y1 - yy) ** 2)) * sqrt(((x2 - xx) ** 2 + (y2 - yy) ** 2))
                    res = min(res, area)
                seen[(centerX, centerY, diagonal)].append((x1, y1))
        
        
        # print(seen)
        return res if res < math.inf else 0