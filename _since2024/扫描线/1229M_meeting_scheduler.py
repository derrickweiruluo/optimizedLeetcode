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
"""

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = 0
        j = 0
        len_slot1 = len(slots1)
        len_slot2 = len(slots2)

        while i < len_slot1 and j < len_slot2:
            intersact_start = max(slots1[i][0], slots2[j][0])
            intersact_end = min(slots1[i][1], slots2[j][1])
            if intersact_end - intersact_start >= duration:
                return [intersact_start, intersact_start + duration]
            elif slots1[i][1] < slots2[j][1]:  # moving condition is while tail is trailing
                i += 1
            else:
                j += 1
