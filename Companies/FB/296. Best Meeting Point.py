'''
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''




class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        # Median Therom, O(MN) for Both
        # https://leetcode.com/problems/best-meeting-point/discuss/74189/Am-I-the-only-person-who-don't-know-why-median-could-give-shortest-distance
        '''the absolute deviations at a certain position is weighted by the number of points that are actually at this position. If we have a bunch of coordinates, and at each coordinate, there is exactly one point, then the optimal solution is definitely the middle point. But now, in a single row or column, there may exist multiple points. So, the optimal solution should be biased towards the region with denser points.

        As a simple example, suppose the coordinates are 0, 50 and 100. If there are one point at each position respectively, then the meeting point would be 50, definitely. But suppose there are 1000 points at 0, and other two points each at 50 and 100, respectively. Of course, you'll have to choose 0 as the meeting point. Otherwise, the 1000 points at coordinate 0 will have to move to at least 50.'''
        
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        # 按频率，row & col 从小到大， 分别记录 bldg的 x, y 坐标，
        # 然后根据 median therom， 取两者的中位数，就是解(MATH)
        xCords = [i for i in range(m) for j in range(n) if grid[i][j]]
        yCords = [j for j in range(n) for i in range(m) if grid[i][j]]
        # print(xCords)
        # print(yCords)
        midRow = xCords[len(xCords) // 2]
        midCol = yCords[len(yCords) // 2]
        
        
        # print(midRow, midCol)
        return sum(abs(x - midRow) for x in xCords) + sum(abs(y - midCol) for y in yCords)
        