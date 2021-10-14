'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.



Think Outside of The Box!
Intuitively, you will try to solve it based on the solution of 3Sum.
But... Build a map for counting different sums of two numbers. The rest of things are straightfoward.

https://leetcode.com/problems/3sum-with-multiplicity/discuss/181128/10-lines-Super-Super-Easy-Java-Solution

'''

class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        # counter = collections.Counter(nums)
        twoSums = collections.defaultdict(int)
        mod = 1000000007
        res = 0
        
        for i in range(len(nums)):
            # at cur idx, += the compliment occurrence before this idx
            res = (res + twoSums[target - nums[i]]) % mod

            # for j from o to i - 1, update the twoSum compliment before advancing to
            # the next idx
            for j in range(i):
                twoSums[nums[i] + nums[j]] += 1
        
        return res % mod