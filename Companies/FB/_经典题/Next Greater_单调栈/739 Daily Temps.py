'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


找多少天后，温度会升高
'''

### 古城单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()  # stack pop 掉 小于等于当前温度的日子，维持mono-increase stack
            res[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
        
        return res




# Monostack 解法
# with stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # increasing stack of (idx, temp)
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res

# O(1) Space 解法
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for d in range(n - 2, -1, -1):
            next_day = 1
            while next_day and temperatures[d + next_day] <= temperatures[d]: # while next_node and next_node.val <= curr_node.val
                if res[d + next_day]:
                    next_day += res[d + next_day]

                else:
                    next_day = 0
            res[d] = next_day

        return res


