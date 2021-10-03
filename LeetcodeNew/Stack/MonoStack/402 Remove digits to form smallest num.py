'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

##Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # 生成最小递增序列，每次出现更小的时候我们就把前面的更大的值替换掉，可替换次数有限不能超过k
        stack = []  # mono-increasing stack
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k > 0:
            stack = stack[:-k]  # remove the last k in the mono-increasing stack
        
        res = ''.join(stack).lstrip('0')  # remove leading zeros
        return res if res else '0'