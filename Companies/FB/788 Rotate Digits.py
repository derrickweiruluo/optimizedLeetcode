'''
Rotate Each digit in a num 180, check if you get a valid diff num

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].
'''

class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        mapping = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2, 6: 9, 9: 6}
        res = 0
        
        for i in range(1, n + 1):
            cur = list(map(int, str(i)))
            rotated = [0] * len(cur)
            flag = True
            # print(cur)
            for idx, digit in enumerate(cur):
                if digit not in mapping: 
                    flag = False
                    break
                rotated[idx] = mapping[digit]
            if flag and cur != rotated:
                res += 1
        
        return res