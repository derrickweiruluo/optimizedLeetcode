"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.


Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

"""

class Solution1:   # time NlogN, space 1
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        """
        Solution 1: Just Sort, O(NlogN)
        Sort the input array.
        Compared with previous number,
        the current number need to be at least prev + 1.

        Time Complexity: O(NlogN) for sorting
        Space: O(1) for in-space sort

        Note that you can apply "O(N)" sort in sacrifice of space.
        Here we don't talk further about sort complexity.
        """
        
        count, next_num = 0, 0
        
        for num in sorted(nums):
            count += max(0, next_num - num)
            next_num = max(next_num + 1, num + 1)
        
        return count
      
 
"""
Solution 2, O(KlogK)
Same idea as solution 1 above.
But instead of assign value one by one,
we count the input numbers first, and assign values to all same value at one time.

This solution has only O(N) time for cases like [1,1,1,1,1,1,.....]

Time Complexity:
O(NlogK) using TreeMap in C++/Java
O(N + KlogK) using HashMap in Python
Space: O(K) for in-space sort
"""


    def minIncrementForUnique(self, A):
        c = collections.Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res

      
"""
Solution 3: Union Find, O(N)
Time: Amortized O(N)
Space: O(N)
"""
    
    def minIncrementForUnique(self, A):
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in A)
