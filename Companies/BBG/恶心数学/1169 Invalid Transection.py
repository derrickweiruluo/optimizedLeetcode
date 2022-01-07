'''
A transaction is possibly invalid if:

1.  the amount exceeds $1000, or;
2.  if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
'''
import collections

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # transactions: 'name, time, amount, city'
        
        # defualtdict 的快捷写法
        memo = collections.defaultdict(lambda: collections.defaultdict(set))
        res = []
        
        for i, s in enumerate(transactions):
            lst = s.split(',')
            name, time, amount, city = lst[0], int(lst[1]), int(lst[2]), str(lst[3])
            memo[time][name].add(city)

        
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
                if len(memo[t][name]) > 1 or city not in memo[t][name]:
                    res.append(s)
                    if name == 'iris': print(memo[t])
                    break
                    
        return res




class Solution:  # 用普通 dict, too wordy
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # transactions: 'name, time, amount, city'
        
        # mapping of {timeStamp: {name: set(unique city name)}}
        memo = {}
        res = []
        
        for i, s in enumerate(transactions):
            lst = s.split(',')
            name, time, amount, city = lst[0], int(lst[1]), int(lst[2]), str(lst[3])
            if time not in memo:
                memo[time] = {name: set()}
                memo[time][name].add(city)
            else:
                if name not in memo[time]:
                    memo[time][name] = set()
                    memo[time][name].add(city)
                else:
                    memo[time][name].add(city)
        
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
                if len(memo[t][name]) > 1 or city not in memo[t][name]:
                    res.append(s)
                    if name == 'iris': print(memo[t])
                    break
                    
        return res
                

["iris,34,475,singapore", "iris,291,33,mexico", "iris,967,965,chicago", "iris,71,453,guangzhou", "iris,512,87,chicago", "iris,714,835,amsterdam", "iris,81,1715,amsterdam", "iris,210,1667,shanghai", "iris,753,169,frankfurt", "iris,527,708,mexico"]