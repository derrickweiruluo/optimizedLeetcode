'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''


# 给一组 温度日期数组，求 每一天，多少天后温度会变暖


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0 for _ in range(n)]

        for d in range(n - 2, -1, -1):
            next_day = 1
            while next_day and temperatures[d + next_day] <= temperatures[d]: # while next_node and next_node.val <= curr_node.val
                if res[d + next_day]:
                    next_day += res[d + next_day]

                else:
                    next_day = 0
            res[d] = next_day

        return res
        

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monostack 解法
        n = len(temperatures)
        res = [0] * n
        stack = [] # increasing stack of (idx, temp)
        
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                prev = stack.pop()[0]
                res[prev] = i - prev
            stack.append((i, temperatures[i]))
        
        return res