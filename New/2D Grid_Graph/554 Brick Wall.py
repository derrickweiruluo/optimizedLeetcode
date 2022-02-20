'''
https://leetcode.com/problems/brick-wall/
'''


# cutting brick wall, return min-cut of bricks

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        counter = collections.defaultdict(int)
        for i in range(len(wall)):
            brickLength = 0

            # do not iterate the last column, since cannot be cut
            for j in range(len(wall[i]) - 1):  
                brickLength += wall[i][j]
                counter[brickLength] += 1
                # brickLength += wall[i][j]
        
        print(counter)
        # 假如每一行只有一块砖头, 那 res == num of rows
        return len(wall) - max(counter.values() or [0])




class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        counter = collections.defaultdict(int)
        for row in wall:
            rowSum = row[0]
            for j in range(1, len(row)):
                counter[rowSum] += 1
                rowSum += row[j]
        
        return len(wall) - max(counter.values() or [0])



