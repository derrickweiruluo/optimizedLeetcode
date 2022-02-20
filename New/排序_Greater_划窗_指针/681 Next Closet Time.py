'''
Give a current time 'HH:MM'

Return the next closest time, wrap to the next day if needed

'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        
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