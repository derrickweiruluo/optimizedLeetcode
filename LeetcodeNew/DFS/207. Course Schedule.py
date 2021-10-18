"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Comlexity. We use classical dfs, so:
time comlexity is O(E+V), where E is number of edges and V is number of vertices. 
Space complexity is also O(E+V) because we work with adjacency lists
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # top down approach, search from high-level course to low-level
        # if search to the leaf course, return True and mark as True
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return False
        return True
    
    def dfs(self, course, graph, visited):
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True
        visited[course] = -1
        for preq in graph[course]:
            if not self.dfs(preq, graph, visited):
                return False
        
        visited[course] = 1
        return True