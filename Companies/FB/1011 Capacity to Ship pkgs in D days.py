'''
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
'''




'''
Time complexity: O(n * log(sum(weights))
Time complexity: O(n * logSIZE), 
where SIZE is the size of the search space (sum of weights - max weight).
which is the left, right bound
Space complexity: O(1).
'''
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        left, right = max(weights), sum(weights)
        
        def valid(load, weights):
            res = 1
            cur = 0
            for w in weights:
                if cur + w > load:
                    cur = 0
                    res += 1
                cur += w
            return res <= days
        
        
        while left < right:
            mid = (left + right) // 2
            if not valid(mid, weights):
                left = mid + 1
            else:
                right = mid
        
        return left