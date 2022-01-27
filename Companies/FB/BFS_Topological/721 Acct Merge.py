'''
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
'''

# Time O(NK log NK)
# Space O(NK)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        visited = set()
        
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                # {unique_email: idx_of_acct}
                graph[email].add(i)
                
                
        def dfs(i, emailSet):
            # emailSet updated thru out the dfs
            if i in visited:
                return
            visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emailSet.add(email)
                for k in graph[email]:
                    dfs(k, emailSet)
                    
        res = []
        for i, acct in enumerate(accounts):
            if i not in visited:
                
                # Each dfs call initialize a empty set, pass into
                # the dfs calls, and get updated, added to the res
                name, emailSet = acct[0], set()
                dfs(i, emailSet)
                res.append([name] + sorted(list(emailSet)))
        
        return res