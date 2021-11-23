# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if i == candidate:
                continue
            # The definition of a celebrity is that all the other n - 1 people know him/her, 
            # but he/she does not know any of them.
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        
        return candidate
        