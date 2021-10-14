'''
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.


Just store every start index for each value and at end index plus one minus it
https://leetcode.com/problems/range-addition/discuss/84217/Java-O(K-%2B-N)time-complexity-Solution
'''

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, increment in updates:
            res[start] += increment
            if end < length - 1:
                res[end + 1] -= increment
        
        curSum = 0
        for i in range(length):
            curSum += res[i]
            res[i] = curSum
        
        return res
    
    '''
    Just explain res->sum:
    res[0,2,3,0,-5]:
    sum[0] = res[0] = 0;
    sum[1] = res[0] + res[1] = 0 + 2 = 2;
    sum[2] = res[0] + res[1] + res[2] = 0 + 2 + 3 = 5;
    sum[3] = res[0] + res[1] + res[2] + res[3] = 0 + 2 + 3 + 0 = 5;
    sum[4] = res[0] + res[1] + res[2] + res[3] + res[4] = 0 + 2 + 3 + 0 + (-5) = 0;
    '''