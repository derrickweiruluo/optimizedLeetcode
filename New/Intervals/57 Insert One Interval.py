'''
给一个non-overlapping的 intervals， 从小到大按照start time 排序
插进 One interval

Return the new intervals after the insertion
merge intervals when needed
'''

# Clarificaitons:
# 1.    input is already sorted by start time


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # logn
        # 思路：newInterval 和 intervals 玩消消乐
        # 1: 可以消消乐：update newInterval
        # 2: 不可以消消乐：加进res

        # 最后一步只需把updated newInterval 加进 res
        res = []
        for idx, (start, end) in enumerate(intervals):
            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[idx:]
            else:  # update the overlapping interval
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        res.append(newInterval)
        return res


        # nlogn
        intervals.append(newInterval)
        intervals.sort()
        res = []
        
        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res