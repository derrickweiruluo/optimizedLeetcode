'''
Integer to Eng Words
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        oneTo19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
                    'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()
        
        def dfs(n):
            if n < 20:
                return oneTo19[n - 1: n]
            if n < 100:
                return [tens[n // 10 - 2]] + dfs(n % 10)
            if n < 1000:
                return [oneTo19[n // 100 - 1]] + ["Hundred"] + dfs(n % 100)
            
                                               # 1,        2,         3
            for power, word in [[1, "Thousand"], [2, "Million"], [3, "Billion"]]:
            # for power, word in enumerate(("Thousand", "Million", "Billion"), 1):
                if n < 1000 ** (power + 1):
                    return dfs(n // 1000 ** power) + [word] + dfs(n % 1000 ** power)
            
        return " ".join(dfs(num)) or "Zero"