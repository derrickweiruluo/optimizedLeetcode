'''
Input: numerator = 1, denominator = 2
Output: "0.5"

Input: numerator = 2, denominator = 1
Output: "2"

Input: numerator = 4, denominator = 333
Output: "0.(012)"
'''

# O(n) linear time
# O(n) space
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        n, rem = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        
        if rem == 0:
            return sign + str(n)
        
        res = [sign + str(n), "."]
        
        seen = {}  # seen remainder
        
        while rem > 0 and rem not in seen:
            seen[rem] = len(res)  # to specify possible starting index for "("
            n, rem = divmod(rem * 10, abs(denominator))
            res.append(str(n))
            
        # the step to insert the "()", 
        # get the len of the seen(rem) at the first repeating rem
        if rem in seen:
            idx = seen[rem]
            res.insert(idx, "(")
            res.append(")")
        
        # return ''.join(res)
        return ''.join(res).rstrip(".")  # if not checking rem == 0 up front