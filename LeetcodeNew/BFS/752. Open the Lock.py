# Solution 1: Usual bfs
# We can look at this problem as graph problem, where we need to find shortest way between given two nodes. We can do classical bfs to do it.

# Complexity
# The worst time complexity is O(E), where E is number of edges and it can be 10000 * 8/2, because we have 10000 nodes and each node is connected with 8 others. 
# Space complexity O(N), where N is size of deadends.

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)
        queue = collections.deque([(0, "0000")])
        
        if "0000" in dead: return -1
        
        while queue:
            steps, code = queue.popleft()
            if code == target:
                return steps
            
            for i in range(4):
                digit = int(code[i])
                for next_digit in (digit - 1) % 10, (digit + 1) % 10:
                    next_code = code[:i] + str(next_digit) + code[i + 1:]
                    if next_code not in dead:
                        dead.add(next_code)
                        queue.append((steps + 1, next_code))
                        
        
        return -1
