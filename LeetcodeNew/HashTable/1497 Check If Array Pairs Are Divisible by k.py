'''
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.


Ex 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Ex 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Ex 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
'''

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        rem = collections.defaultdict(int)
        
        for i, num in enumerate(arr):
            rem[num % k] += 1
        
        res = 0
        for i in range(1, k):
            left, right = i, k - i
            if rem[left] != rem[right]:
                return False
            if left == right:
                return rem[left] % 2 == 0
        
        return rem[0] % 2 == 0