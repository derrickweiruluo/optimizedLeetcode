'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

'''

# Clarifications:
# All the given points are unique.

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        seen = set()
        res = math.inf
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    res = min(res, area)
            # has to add after the look up, 
            # since this point must not be used during check up
            seen.add((x1, y1))
        
        return res if res < math.inf else 0




# O(N^1.5)
# For each x value in sorted order, check all y pairs.
# However, it seems that, in the test cases, it has a really big amount of rectangles.
# In these worst cases, the time complexity is O(nx * nx * ny) < O(N ^ 1.5).

# In the extreme worst cases, like all points have x = 0 or y = 0

def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0