"""
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

#####
input is pre-sorted, 扫描线基操

一共三种情况：
a: 完全无交集， 直接append to res
b: 完全重合， 直接skip当下的iteration
c: 部分重合：
  if: 当前iteration的右边被重合，append left partial
  if: 当前iteration的左边被重合，append right partial
  双if是因为，有时候当前iteration会被剪成两半，所以要考虑是不是去掉重合会产生左右碎片
  
1 <= intervals.length <= 104
-109 <= ai < bi <= 109
"""
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        res = []
        
        for start, end in intervals:
            if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                res.append([start, end])
            elif start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            else:
                if start < toBeRemoved[0] < end:
                    res.append([start, toBeRemoved[0]])
                if start < toBeRemoved[1] < end:
                    res.append([toBeRemoved[1], end])
        
        return res
