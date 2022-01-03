'''
给一串会议时间，问需要多少个房间
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # res = 0
        intervals.sort(key = lambda x: (x[0], x[1]))
        heap = [intervals[0][1]]  # heap of earliest-finished meeting
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappushpop(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        
        return len(heap)