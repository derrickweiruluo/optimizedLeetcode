'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

'''
class Solution:  # Topological Sort
    # time O (E + V)
    # Space O (E + V)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        count = 0
        res = []
        queue = collections.deque(x for x in range(numCourses) if not indegree[x])
        while queue:
            cur = queue.popleft()
            res[count] = cur
            count += 1
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)

    
        # return count == numCourses
        return res



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)] # storing [0, -1, 1] values only
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        self.res = []
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return []
        return self.res
    
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
        self.res.append(course)
        return True
        