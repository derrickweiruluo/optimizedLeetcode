# Intuition:
# Consider trust as a graph, all pairs are directed edge.
# The point with in-degree - out-degree = N - 1 become the judge.

# Explanation:
# Count the degree, and check at the end.

# Time Complexity:
# Time O(T + N), space O(N)


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count = [0] * (n + 1)
        
        for person, trusted in trust:
            count[person] -= 1
            count[trusted] += 1
        
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        
        return -1
