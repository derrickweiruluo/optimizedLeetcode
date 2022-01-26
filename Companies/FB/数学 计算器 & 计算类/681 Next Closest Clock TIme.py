'''
Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.


Input: time = "23:59"
Output: "22:22"  -> wrap around to next day
'''


class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        # You may assume the given input string is always valid. 
        # For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
        
        hour, minute = time.split(":")
        
        seen = sorted(set(hour + minute))
        values = [a + b for a in seen for b in seen] # all possible combo, at most 16
        
        # Try inc the minute first, if fail, try the hour
        i = values.index(minute)
        if i < len(values) - 1 and values[i + 1] < "60":
            return hour + ":" + values[i + 1]
        
        # try inc the hour since previous try fail, if fail again, return next day's smallest
        i = values.index(hour)
        if i < len(values) - 1 and values[i + 1] < "24":
            return values[i + 1] + ":" + values[0]
        
        # if above failed, return next day's smallest (wrap around)
        return values[0] + ":" + values[0]