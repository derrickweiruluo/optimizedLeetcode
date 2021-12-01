# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        cur = 40
        while cur >= 40:
            cur = (rand7() - 1) + (rand7() - 1) * 7
        
        return cur % 10 + 1
        