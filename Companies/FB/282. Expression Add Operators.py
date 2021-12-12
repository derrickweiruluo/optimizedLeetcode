'''
Given a string num that contains only digits and an integer target, return all possibilities 
to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.ß
'''

class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        
        def backtrack(i, path, cur, prev):
            if i == len(s):
                if cur == target:
                    ans.append(path)
                return

            for j in range(i, len(s)):
                if j > i and s[i] == '0': break  # Skip leading zero number
                num = int(s[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(num), cur + num, num)  # First num, pick it without adding any operator
                else:
                    backtrack(j + 1, path + "+" + str(num), cur + num, num)
                    backtrack(j + 1, path + "-" + str(num), cur - num, -num)
                    
                    # keep the prevNum so that to calculate cur, we need to minus prev then Plus with prev * num. 
                    # So cur = cur - prev + prev * num. e.g. Can imagine with example: 1+2*3*4
                    backtrack(j + 1, path + "*" + str(num), cur - prev + prev * num, prev * num)

        ans = []
        backtrack(0, "", 0, 0)
        return ans