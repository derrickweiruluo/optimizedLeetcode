'''
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        h = hour * 30 + minutes / 60 * 30
        m = minutes / 60 * 360
        
        diff = abs(h - m)
        return diff if diff < 180 else 360 - diff