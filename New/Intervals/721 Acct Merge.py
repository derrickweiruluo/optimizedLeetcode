'''
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
'''

# UF
class Solution:
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a > b:
            self.parents[a] = b  
        else: 
            self.parents[b] = a
    
    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        self.parents = {i: i for i in range(len(accounts))}
        
        emailMapping = {}
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in emailMapping:
                    self.union(emailMapping[email], i)
                else:
                    emailMapping[email] = i
        
        acctMapping = {}
        for email in emailMapping:
            acct = self.find(emailMapping[email])
            if acct in acctMapping:
                acctMapping[acct].append(email)
            else:
                acctMapping[acct] = [email]
        
        res = []
        for parent in acctMapping:
            res.append([accounts[parent][0]] + sorted(acctMapping[parent]))
        return res


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