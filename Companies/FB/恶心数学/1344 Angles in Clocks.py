'''
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        h = hour % 12 * 30 + minutes / 60 * 30
        m = minutes / 60 * 360
        
        if abs(h - m) > 180:
            return 360 - abs(h - m)
        return abs(h - m)