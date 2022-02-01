'''
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
'''


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
            # queue as the window for comparison, comparing nums[i] with queue[0] when i - queue[0] <= k
            if queue and i - queue[0] == k:
                queue.popleft()
                
            while queue:
                # pop useles elements from last/right of the queue
                if nums[queue[-1]] < nums[i]:
                    queue.pop()
                else:
                    break  # top of the queue already the win's max
    
            queue.append(i)
            # print(len(queue) < k + 1)
            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res