class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            # a = asteroid
            while stack and asteroid < 0 and stack[-1] > 0:
                # print(a)
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                elif abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) < stack[-1]:
                    break
            else:
                # print("##" + str(a))
                stack.append(asteroid)
        
        return stack
