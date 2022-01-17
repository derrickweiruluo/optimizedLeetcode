'''
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # dict 中 dict
        mapping = collections.defaultdict(dict)

        for (x, y), v in zip(equations, values):
            mapping[x][y] = v
            mapping[y][x] = 1 / v
        
        def bfs(dividend, divisor):
            if not dividend in mapping and not divisor in mapping:
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