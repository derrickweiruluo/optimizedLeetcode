'''
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Ex 1:
Input: arr = [3,1,3,6]
Output: false
Ex 2:

Input: arr = [2,1,2,6]
Output: false
Ex 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Ex 4:
Input: arr = [1,2,4,16,8,4]
Output: false

######
1. We sort our number with key abs(x).
2. Also we create cnt is Counter of all numbers: it can happen that we have some numbers several times.
3. Iterate through sorted arr and if we see that frequency of some number is already 0: it can happen, because this number can be taken, we do nothing. If it is not zero, but we do not have pair 2*num, return False. Finally, we decreasy frequencies of two numbers: num and 2*num.

Complexity
It is O(n log n) to sort number and then O(n) to put them all into pairs, so overall time complexity is O(n log n). Space complexity is O(n).

'''

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        numCounter = collections.Counter(arr)
        
        # iterate the arr, sorted by abs(num)
        for num in sorted(arr, key = lambda x: abs(x)):
            if numCounter[num] == 0:
                continue
            if numCounter[2 * num] == 0:
                return False
            numCounter[num] -= 1
            numCounter[2 * num] -= 1
        
        return True