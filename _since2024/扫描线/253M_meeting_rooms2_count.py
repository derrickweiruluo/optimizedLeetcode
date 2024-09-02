"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.


Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        starts = []
        ends = []
        for i in range(n):
            starts.append(intervals[i][0])
            ends.append(intervals[i][1])
        starts.sort()
        ends.sort()

        counter = 0
        # counter是计算同一时间内最多的meeting room的数量
        # AKA meeting overlapping的数量，所以不用在意这个结束时间是属于哪个meeting
        # 相似于同一时间，天空的最大飞机数目
        # prerequisite: starts, ends ARE SORTED
        j = 0
        for i in range(n):
            if starts[i] < ends[j]:
                counter += 1
            else:
                j += 1
        return counter
