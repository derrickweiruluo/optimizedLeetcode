'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Input: intervals = [[7,10],[2,4]]
Output: true
'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) < 2: return True
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        
        return True