'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
 

Constraints:

1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500

#######
注意contraints给的boundary，这意味着
left = max(arr), right = sum(arr)

子方程计算所需时间, 
res from 1 
reset to cur weight when exceeded the limit
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        
        def timeTaken(weights, mid):
            res = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > mid:
                    res += 1
                    cur = w
            return res
        
        
        while left < right:
            mid = (left + right) // 2
            if timeTaken(weights, mid) > days:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    
