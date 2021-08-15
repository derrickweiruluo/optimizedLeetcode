"""
You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point [0, 0], and you are given a destination point target = [xtarget, ytarget], which you are trying to get to. There are several ghosts on the map with their starting positions given as an array ghosts, where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. All inputs are integral coordinates.

Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the four cardinal directions: north, east, south, or west or stay still. All actions happen simultaneously.
You escape if and only if you can reach the target before any ghost reaches you. If you reach any square (including the target) at the same time as a ghost, it does not count as an escape.
Return true if it is possible to escape, otherwise return false.

Example 1:
Input: ghosts = [[1,0],[0,3]], target = [0,1]
Output: true
Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.

Example 2:
Input: ghosts = [[1,0]], target = [2,0]
Output: false
Explanation: You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

########
It's worth noting that what the problem is asking. It asked whether the pacman can escape while it does not require the pacman being catch by ghosts.
So, if I were a ghost, I don't really care where the pacman is or try to catch it. I just go directly to the target and so the pacman has no way to escape.

"""
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        x, y = target
        dist = abs(x) + abs(y)
        for i, j in ghosts:
            if abs(i - x) + abs(j - y) <= dist:
                return False
            
        return True
        
