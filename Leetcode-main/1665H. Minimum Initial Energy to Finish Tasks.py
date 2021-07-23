class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda a: (a[1] - a[0])). # 亮点
        res = 0
        for actual, minimum in tasks:
            res = max(res + actual, minimum)
        return res
