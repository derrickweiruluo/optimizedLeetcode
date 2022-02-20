'''
给一串会议时间，问需要多少个房间
'''

class Solution:  # heap Best 标准解法
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



class Solution:  # 古城数飞机 Best高级解法
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mapping = []
        for interval in intervals:
            mapping.append(interval[0], 1)
            mapping.append(interval[1], -1)
        
        mapping.sort() # by start time then end time
        res = count = 0
        for meeting in mapping:
            count += meeting[1]
            res = max(res, count)
        
        return res





#*-------------------------------
class Solution:  # 古城数飞机 第二种高级解法
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        
        starts.sort() # by start time then end time
        ends.sort()
        res = end = 0
        for i in range(len(starts)):
            if starts[i] < ends[end]:
                res += 1
            else:
                end += 1
        
        return res