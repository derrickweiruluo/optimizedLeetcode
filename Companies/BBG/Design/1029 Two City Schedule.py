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

# BEST, Time O(N) with quickSelect, Space logN due to recursive stack
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        def diff(cost): # comparator, to seperate
            return cost[0] - cost[1]
        
        
        def partition(nums, start, end):
            # use start, end for partition zone

            if start == end: 
                i = start
            else:
                # index i is the left-advancing index to get Kth-Largest
                i, rand_idx = start, random.randint(start, end)
                nums[end], nums[rand_idx] = nums[rand_idx], nums[end]
                for j in range(start, end):
                    if diff(nums[j]) < diff(nums[end]):
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                nums[end], nums[i] = nums[i], nums[end]
            
            n = len(nums)
            if i == n // 2: # if the partition stop at the mediam --> answer
                res = 0
                for k in range(i):
                    res += nums[k][0] + nums[k + n // 2][1]
                return res
            elif i < n // 2:
                return partition(nums, i + 1, end)
            else:
                return partition(nums, start, i - 1)
            
        
        return partition(costs, 0, len(costs) - 1)


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