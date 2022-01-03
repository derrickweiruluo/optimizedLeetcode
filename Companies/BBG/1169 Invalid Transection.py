'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
'''

class Solution: # Both O(N)
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # transactions: 'name, time, amount, city'
        
        # mapping = collections.defaultdict(list)
        # time = int(transactions[0].split(',')[1])
        
        
        memo = {}  # {time: {name: [list of cities]}}
        res = []
        
        for i, s in enumerate(transactions):
            lst = s.split(',')
            name, time, amount, city = lst[0], int(lst[1]), int(lst[2]), lst[3]
            if time not in memo:
                memo[time] = {name: [city]}
            else:
                if name not in memo[time]:
                    memo[time][name] = [city]
                else:
                    memo[time][name].append(city)
        
        for i, s in enumerate(transactions):
            lst = s.split(',')
            name, time, amount, city = lst[0], int(lst[1]), int(lst[2]), lst[3]
            
            if amount > 1000:
                res.append(s)
                continue
            for t in range(time - 60, time + 61):
                if t not in memo:
                    continue
                if name not in memo[t]:
                    continue
                if len(memo[t][name]) > 1 or memo[t][name][0] != city:
                    res.append(s)
                    break
        
        return res
                