"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 
Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

###########

To use two variables 'up' and 'down' to count the steps of continuous up and down respectively, and a 'peak' representing the peak before going down. In the below example:  [0, 1, 20, 20, 9, 8, 7]

"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if len(ratings) == 0: return 0
        up = down = peak = 0
        res = 1
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                res += 1 + up
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                res += 1
            else:
                up = 0
                down += 1
                res += down
                if down > peak:  # give peak one more candy since down > peak
                    res += 1
        
        return res
                
