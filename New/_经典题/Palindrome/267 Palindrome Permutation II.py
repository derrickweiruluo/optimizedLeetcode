'''
Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
'''

# Time O(N !) for permutation, O(N) for recursion depth
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        counter = collections.Counter(s)
        mid = [k for k, v in counter.items() if v % 2]
        
        if len(mid) > 1: return []
        mid = '' if not mid else mid[0]
        half = ''.join([k * (v // 2) for k, v in counter.items()])
        half = [s for s in half]
        
        def backtrack(length, path):
            if len(path) == length:
                cur = ''.join(path)
                res.append(cur + mid + cur[::-1])
            else:
                for i in range(length):
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    path += [half[i]]
                    backtrack(length, path)
                    visited[i] = False
                    path.pop()
        
        
        res = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return res