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



# Clarifications:
# 1.    The robot starts at an unknown location in the root that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.
# 2.    The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
# 3.    When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

'''To indicate whether a cell has been cleaned(visited), we assume the start poin is (0, 0) and initial orientation is 0 as follows

    0
3  -|-  1
    2
    
each orientation is associated with a direction. 
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]; indicates movement.
'''

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.clean(robot, 0, 0, 0, set())
    

    # Using DFS, we have to backtrack after we explore as far as possible along a branch, i.e. robot moves backward one step while maintaining its orientation.
    def clean(self, robot, x, y, curDir, visited):
        robot.clean()
        visited.add(str(x) + "#" + str(y))
        for i in range(curDir, curDir + 4):
            xi = self.dirs[i % 4][0] + x
            yi = self.dirs[i % 4][1] + y
            if (str(xi) + "#" + str(yi)) not in visited and robot.move():
                self.clean(robot, xi, yi, i % 4, visited)
            robot.turnRight()
        
        # Moves backward one step while maintaining the orientation.
        robot.turnRight()
        robot.turnRight()
        robot.move()        # return False if facing a wall, return True if not
        robot.turnRight()
        robot.turnRight()
        robot.turnRight()