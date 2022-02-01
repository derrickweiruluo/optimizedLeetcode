'''
https://leetcode.com/problems/process-restricted-friend-requests/




Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
Output: [true,false]
Explanation:
Request 0: Person 0 and person 2 can be friends, so they become direct friends. 
Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
'''

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        union = {i : i for i in range(n)}
        rank = {i: 0 for i in range(n)}
        
        def find(x):
            if x != union[x]:
                union[x] = find(union[x])
            return union[x]
        
        
        res = []
        
        for u, v in requests:
            success = True
            parent_u, parent_v = find(u), find(v)
            if parent_u != parent_v:
                for x, y in restrictions:
                    parent_x, parent_y = find(x), find(y)
                    if (parent_x, parent_y) in [(parent_u, parent_v), (parent_v, parent_u)]:
                        success = False
                        break
            
            if success:
                if rank[parent_u] < rank[parent_v]:
                    union[parent_u] = parent_v
                else:
                    union[parent_v] = parent_u
                    if rank[parent_u] == rank[parent_v]:
                        rank[parent_u] += 1
            
            res.append(success)
        
        return res