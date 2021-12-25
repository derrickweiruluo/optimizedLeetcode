# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

'''
https://leetcode.com/problems/robot-room-cleaner/discuss/153530/DFS-Logical-Thinking
'''

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.clean(robot, 0, 0, 0, set())
        
    def clean(self, robot, x, y, curDir, visited):
        robot.clean()
        visited.add(str(x) + "#" + str(y))
        for i in range(curDir, curDir + 4):
            xi = self.dirs[i % 4][0] + x
            yi = self.dirs[i % 4][1] + y
            if (str(xi) + "#" + str(yi)) not in visited and robot.move():
                self.clean(robot, xi, yi, i % 4, visited)
            robot.turnRight()
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()