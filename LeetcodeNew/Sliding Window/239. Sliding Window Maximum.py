"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:
Input: nums = [9,11], k = 2
Output: [11]

Example 5:
Input: nums = [4,-2], k = 2
Output: [4]
"""


"""
solution of monotonic stack
Sliding window minimum/maximum = monotonic queue. I smelled the solution just when I read the title.
This is essentially the same idea as others' deque solution, but this is much more standardized and modulized. 

push: push an element into the queue; O (1) (amortized)
pop: pop an element out of the queue; O(1) (pop = remove, it can't report this element)
max: report the max element in queue;O(1)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # deque of store each window's max's idx in the arr
        queue = collections.deque()
        res = []
        
        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if queue and i - queue[0] == k:
                queue.popleft()
                
            while queue:
                # pop useles elements from last/right of the queue
                if nums[queue[-1]] < nums[i]:
                    queue.pop()
                else:
                    break  # top of the queue already the win's max
    
            queue.append(i)
        
            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res
