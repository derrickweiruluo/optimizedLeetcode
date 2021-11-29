'''
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.
'''

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        '''
        There is a pattern for it, when n = 9
        1th : 1 1 1 1 1 1 1 1 1 
        2nd : 1 0 1 0 1 0 1 0 1
        3rd : 1 0 0 0 1 1 1 0 0
        4th : 1 0 0 0 0 1 1 0 1
        5th : 1 0 0 0 1 1 1 0 1
        6th : 1 0 0 0 1 0 1 0 1
        7th : 1 0 0 0 1 0 0 0 1
        8th : 1 0 0 0 1 0 0 1 1
        9th : 1 0 0 0 1 0 0 1 0  --> 3
        '''

        # You can see that, after each round, all bulbs before that round will not be touched anymore.
        return math.floor(n ** 0.5) # perfect square
        # return int(n ** 0.5)