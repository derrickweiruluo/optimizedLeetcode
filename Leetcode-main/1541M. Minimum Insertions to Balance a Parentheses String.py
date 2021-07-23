class Solution:
  #超低频， FB only
    def minInsertions(self, s: str) -> int:
        compliment, right = 0, 0
        for char in s:
            if char == '(':
                right += 2
                if right % 2:   # when 奇数, , then compliment to makeup
                    right -= 1    # make right even first by -=1
                    compliment += 1   # makeup right by compliment += 1
            else:
                right -= 1
                if right < 0:
                    right += 2
                    compliment += 1 # makeup left by compliment += 1
        
        return right + compliment
