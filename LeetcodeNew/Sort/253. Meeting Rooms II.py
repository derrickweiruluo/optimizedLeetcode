"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        heap = [].  # heap of end time
        
        for start, end in intervals:
            # if the current start time >= earliest finish time in heap: heaprepleace(heap, end) 
            if heap and start >= heap[0]:
                heapq.heapreplace(heap, end)
            # add end to heap
            else:
                heapq.heappush(heap, end)
        
        return len(heap)
