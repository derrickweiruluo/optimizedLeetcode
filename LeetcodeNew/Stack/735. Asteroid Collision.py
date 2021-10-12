'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 
Ex 1:
Input: asteroids = [5,10,-5]
Output: [5,10]

Ex2:
Input: asteroids = [8,-8]
Output: []

Ex 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                elif abs(asteroid) < stack[-1]:
                    break
                elif abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
            else:
                stack.append(asteroid)
        
        
        return stack