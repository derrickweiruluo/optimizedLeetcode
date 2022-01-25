'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
'''
class Solution:  # Topological Sort
    # time O (E + V)
    # Space O (E + V)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        count = 0
        queue = collections.deque(x for x in range(numCourses) if not indegree[x])
        while queue:
            cur = queue.popleft()
            count += 1
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)

    
        return count == numCourses



class Solution:  # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
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