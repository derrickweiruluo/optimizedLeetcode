'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        # You may assume the given input string is always valid. 
        # For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
        
        hour, minute = time.split(":")
        
        seen = sorted(set(hour + minute))
        values = [a + b for a in seen for b in seen] # all possible combo, at most 16
        
        i = values.index(minute) # 先检测分钟，找合理解
        if i + 1 < len(values) and values[i + 1] < "60":
            return hour + ":" + values[i + 1]
        
        i = values.index(hour)  # 再检测小时，找合理解
        if i + 1 < len(values) and values[i + 1] < "24":
            return values[i + 1] + ":" + values[0]
        
        
        return values[0] + ":" + values[0]  # 当天没有解的话, warp around to next day