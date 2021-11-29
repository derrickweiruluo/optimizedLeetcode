'''
accounts [name, email_1, email_2, email_3, email 4]
Merge account if there is any match within the list of emails
the return account's email lists are sorted

'''

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        visited = [False] * len(accounts)
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                graph[email].add(i)
        
        def dfs(idx, email_set):
            if visited[idx]:
                return
            visited[idx] = True
            for j in range(1, len(accounts[idx])):
                email = accounts[idx][j]
                email_set.add(email)
                for k in graph[email]:
                    dfs(k, email_set)
        
        res = []
        for i, acct in enumerate(accounts):
            if visited[i]:
                continue
            name, email_set = acct[0], set()
            dfs(i, email_set)
            res.append([name] + sorted(list(email_set)))
        
        return res