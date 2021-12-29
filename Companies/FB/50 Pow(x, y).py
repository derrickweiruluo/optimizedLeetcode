'''
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

'''
class Solution: # Iterative approach,log(N) time but O(1) space
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        res = 1
        while n:
            # print(n, x)
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n // 2
        
        return res



class Solution:  # both log(N)

    # For each computation, we need to store the result of x ^ (n/2). We need to do the computation for O(logn) times
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1 / x, -n)
        
        half = self.myPow(x, n // 2)
        if n % 2 == 1:
            print(n)
            return half * half * x
        else:
            return half * half




# Complexity: time complexity is O(log n), space complexity for this recursive algorithm is also O(log n), which can be reduced to O(1), if we use iterative approach instead.

class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x