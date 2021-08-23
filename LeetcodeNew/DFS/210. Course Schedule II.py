"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].


Comlexity. We use classical dfs, so: 
time comlexity is O(E+V), where E is number of edges and V is number of vertices. 
Space complexity is also O(E+V) because we work with adjacency lists

"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        self.path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return []
        return self.path
    
    def dfs(self, graph, visited, cur):
        if visited[cur] == -1: return False
        if visited[cur] == 1: return True
        visited[cur] = -1   
#         先标记为 -1 直到最深的 被标记为1 （leaf），
#         往上的的递归都会变成1 且从底部一直构建path
        for course in graph[cur]:
            if not self.dfs(graph, visited, course):
                return False
        
        visited[cur] = 1
        self.path.append(cur)
        return True
