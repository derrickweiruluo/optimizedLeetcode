'''
A company is planning to interview 2* N people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

'''

# https://leetcode.com/problems/two-city-scheduling/discuss/667786/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation
# https://leetcode.com/problems/two-city-scheduling/discuss/278716/C%2B%2B-O(n-log-n)-sort-by-savings




# O(NlogN), O(1)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x : x[0] - x[1])
        n = len(costs)
        res = 0
        for i in range(n // 2):
            res += costs[i][0]
        for i in range(n // 2, n):
            res += costs[i][1]
        
        # the most negative cost will be at front
        # thus res will always subtract the most:
        # which means select the cheapest B
    
        
        return res



# BEST, ave O(N) with quickSelect
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        def diff(cost_pair): # opportunity cost of choosing second cost over first cost
            return cost_pair[0] - cost_pair[1]
        
        def partition(A, start, end):
            if start == end: # the part of an array we are looking at has length 1
                j = start
            else:
                rand_idx = random.randint(start, end-1) # randomize to prevent extreme cases
                A[end], A[rand_idx] = A[rand_idx], A[end]
                i = j = start # QuickSelect
                for i in range(start, end): 
                    if diff(A[i]) < diff(A[end]):
                        A[i], A[j] = A[j], A[i]
                        j += 1
                A[end], A[j] = A[j], A[end]
            
            if j == len(A)//2: # is the median placed in the middle?
                min_cost = 0
                for idx in range(j):
                    min_cost += (A[idx][0] + A[idx+len(A)//2][1])
                return min_cost
            elif j < len(A)//2:
                return partition(A, j + 1, end)
            else:
                return partition(A, start, j - 1)
            
        return partition(costs, 0, len(costs)-1)






# O (nlogN), O(N)space
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff = []
        res = 0
        for costA, costB in costs:
            diff.append(costB - costA)
            res += costA
        
        diff.sort()  
        
        # the most negative cost will be at front
        # thus res will always subtract the most:
        # which means select the cheapest B
        
        n = len(diff)// 2
        for i in range(n):
            res += diff[i]
        
        return res