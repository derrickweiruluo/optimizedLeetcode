'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''
class Solution: # 2nd best
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        # 按照start time 排序，如果res[-1][1] 与 下一个interval的start有重叠，更新res， else append
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res


class Solution: # 2nd best
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #以下写法一样work
        intervals.sort()
        res = []
        
        for i in range(len(intervals)):
            # print(i)
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])
        
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2: return intervals
        
        intervals.sort(key = lambda x: (x[0]))
        i = 0
        j = 1
        while j < len(intervals):
            print(i, j)
            if intervals[j][0] > intervals[i][1]:
                i = j
                j += 1
            else:
                intervals[i][1] = max(intervals[j][1], intervals[i][1])
                intervals.pop(j)
        
        return intervals


class Solution:  # inplace
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # modified in place
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0]) # in-place sorting
        
        prev_index = 0
        curr_index = 1
        while curr_index<len(intervals):
            if intervals[curr_index][0] > intervals[prev_index][1]:
                prev_index = curr_index
                curr_index += 1
            else:
                intervals[prev_index][1] = max(intervals[prev_index][1], intervals[curr_index][1])
                intervals.pop(curr_index) # this should reduce array size, hence no need to increase curr_index
        
        return intervals