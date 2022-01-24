'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b




Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''


"""
Explanation
Assume we are taking A[i] ~ A[i + k -1].
We can binary research i
We compare the distance between x - A[mid] and A[mid + k] - x

@vincent_gui listed the following cases:
Assume A[mid] ~ A[mid + k] is sliding window

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

"""



# constraints: nums is sorted in ASEC order
# If x - A[mid] > A[mid + k] - x,
# it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left, right = 0, len(arr) - k # right is the rightmost startint point
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x: # 如果 leftBound diff > rightBound + 1 diff
                left = mid + 1
            else:
                right = mid
        
        
        # find the left bound of the solution section
        # think of x in between 
        return arr[left: left + k]