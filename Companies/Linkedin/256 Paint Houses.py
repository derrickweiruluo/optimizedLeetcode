'''
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.


 You have to paint all the houses such that no two adjacent houses have the same color.
'''

class Solution:
    
    '''
    Here's the logic. The variables named 'red', 'blue', and 'green' will store running sums of costs as we paint houses. 
    In other words, they store the total cost of painting previous homes.

    cr = the cost of red paint on the current house
    cb = the cost of blue paint on the current house
    cg = the cost of green paint on the current house
    The cost of choosing red paint on the current home is the sum of two things: cr (obviously) + cost of painting the previous home either blue or green. 
    The "min"    chooses the least of those two options.

    Each step of the for-loop is trying all three colors for the current home, and storing the total cost the corresponding running sum.
    '''
    
    def minCost(self, costs):
        red = green = blue = 0
        for curRed, curGreen, curBlue in costs:
            # color_path = current selection + the minimum selection previously
            red, green, blue = curRed + min(green, blue), curGreen + min(red, blue), curBlue + min(red, green)
        
        return min(red, green, blue)