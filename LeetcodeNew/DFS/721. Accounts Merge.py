'''
https://leetcode.com/problems/accounts-merge/

Next, build an emails_accounts_map that maps an email to a list of accounts, which can be used to track which email is linked to which account. This is essentially our graph.

# emails_accounts_map of email to account ID
{
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0],
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}



https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!
https://leetcode.com/problems/accounts-merge/discuss/109157/JavaC%2B%2B-Union-Find
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