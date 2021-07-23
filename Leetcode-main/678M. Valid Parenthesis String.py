class Solution:
    def checkValidString(self, s: str) -> bool:
        closing_max, closing_min = 0, 0
        for i in s:
          # 通过先测'(' 来确保 先open， 若某一个位置不满足， closing_max 就变成负数， 直接return False
          # closing_min 来确保 最后(*)互相抵消
            if i == '(':
                closing_max += 1
                closing_min += 1
                
            if i == ')':
                closing_max -= 1
                closing_min = max(closing_min - 1, 0)
                
            if i == '*':  # max += 1, min -= 1
                closing_max += 1
                closing_min = max(closing_min - 1, 0)
                
            if closing_max < 0:
                return False
            
        # 用最后一步确保在
        return closing_min == 0
