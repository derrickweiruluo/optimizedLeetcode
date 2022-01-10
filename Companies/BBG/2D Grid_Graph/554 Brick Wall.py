'''
https://leetcode.com/problems/brick-wall/
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        counter = collections.defaultdict(int)
        for row in wall:
            rowSum = row[0]
            for j in range(1, len(row)):
                counter[rowSum] += 1
                rowSum += row[j]
        
        return len(wall) - max(counter.values() or [0])