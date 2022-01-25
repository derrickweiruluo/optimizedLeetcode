'''
https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation

We use three flags: met_dot, met_e, met_digit, mark if we have met ., e or any digit so far. First we strip the string, then go through each char and make sure:

If char == + or char == -, then prev char (if there is) must be "eE"
"." cannot appear twice or after "eE"
"eE" cannot appear twice, and there must be at least one digit before and after "eE"
All other non-digit char is invalid

'''


# Valid:      ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", 
               # "-90E3", "3e+7", "+6e-1", "53.5e93"]
# InValid:    ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]


class Solution:
    def isNumber(self, s: str) -> bool:
        
        s = s.lower() # lower and strip spaces
        # .strip(): strip whitespace is needed, but ont in this LC

        seenE = seenDot = seenDigit = False
        for i in range(len(s)):

            if s[i] in '-+':
                if i > 0 and s[i - 1] != 'e': 
                    # this already take care of multiple '-+' cases
                    # or inproper '-+' positions
                    return False
            
            elif s[i] == '.': # dot can be in any where, but only once, not after E
                print(i)
                if seenDot or seenE:
                    return False
                seenDot = True
            
            elif s[i] == 'e': # 'E' can only once and appear after the digit
                if seenE or not seenDigit:
                    return False
                # turn seenE to True, reset seenDigit since after E can start fresh
                # examples: "9.9e2.5" is not valid
                seenE = True
                seenDigit = False
            
            elif s[i].isdigit():
                seenDigit = True
            
            else: # there will be other invalid lowercase letters
                return False
        
        return seenDigit
                