

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: return []
        
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [""]
        for digit in digits:
            res = [p + q for p in res for q in mapping[digit]]
        
        return res