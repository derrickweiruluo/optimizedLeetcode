'''
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
'''


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        mapping = collections.defaultdict(int)
        multiplier = 1
        stack = []
        i = cnt = 0
        elem = ""
        
        for char in formula[::-1]:
            if char.isdigit():
                cnt += int(char) * (10 ** i)
                i += 1
            elif char == ")":
                if i:
                    stack.append(cnt)
                    multiplier *= cnt
                else:
                    stack.append(1)
                i = cnt = 0
            elif char == "(":
                multiplier //= stack.pop()
                i = cnt = 0
            elif char.isupper():
                elem += char
                mapping[elem[::-1]] += (cnt or 1) * multiplier
                elem = ""
                i = cnt = 0
            elif char.islower():
                elem += char
        
        res = []
        for elem, val in sorted(mapping.items()):
            res += elem + (str(val) if val > 1 else "")
        
        return "".join(res)