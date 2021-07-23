class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # corner cases, either num1 or num2 == 0 will return "0"
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)
        
        
        # nested for loop for indexing every digit and update res[i + j] and res[i + j + 1] accordingly
        for i in range(len1)[::-1]:
            for j in range(len2)[::-1]:
                res[i + j + 1] += int(num1[i]) * int(num2[j])
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] %= 10
                
        
        # remove and leading 0 in the res[]
        return "".join(map(str, res)).lstrip("0")
