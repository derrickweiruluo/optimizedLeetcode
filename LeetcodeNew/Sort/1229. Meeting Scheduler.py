"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 
Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
 
Constraints:

1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106


#####
sort both slots by start time
Time: O(MlogM + NlogN) for sorting
Space: O(sorting)
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()
        
        p1 = p2 = 0
        l1, l2 = len(slots1), len(slots2)
        
        while p1 < l1 and p2 < l2:
            intersect_start = max(slots1[p1][0], slots2[p2][0])
            intersect_end = min(slots1[p1][1], slots2[p2][1])
            if intersect_end - intersect_start >= duration:
                return [intersect_start, intersect_start + duration]
            
            # 因为这道题不是p1就是p2增加，p1 绝对增加的条件是p1.end < p2.end, HAVE TO p1 += 1
            elif slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        
        return []
