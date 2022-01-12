'''
cost of move each coin:

i to i + 2 or i - 2 == Cost Zero
i to i + 1 or i - 1 == Cost One
'''

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        even = odd = 0
        
        # Input: position = [2,2,2,3,3]
        # this means, 3 chips on pos 2, 2 chips on pos 3
        
        
        for pos in position:
            if pos % 2 == 0:
                even += 1
            else:
                odd += 1
        
        # move even to even position has no cost
        # thus, the min of (even_count, odd_count) is the amount of coins
        # at the final move, to transfer the "min coins" to the "max pile"
        return min(odd, even)