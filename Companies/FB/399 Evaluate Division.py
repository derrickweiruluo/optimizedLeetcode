'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.


Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            mapping[x][y] = v
            mapping[y][x] = 1 / v
        
        def bfs(dividend, divisor):
            if not (dividend in mapping and divisor in mapping):
                return -1
            curr, visited = [(dividend, 1.0)], set()
            for x, v in curr:
                if divisor == x:
                    return v
                visited.add(x)
                for y in mapping[x]:
                    if y not in visited:
                        curr.append((y, v * mapping[x][y]))
            
            return -1.0
        
        return [bfs(dividend, divisor) for dividend, divisor in queries]
