'''
You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.


Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.


A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.

Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.

Note: If uj and vj are already direct friends, the request is still successful.
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