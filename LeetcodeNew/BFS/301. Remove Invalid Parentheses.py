class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        level = set([s])            # initial BFS as set
        
        while True:
            level_res = []          # smallest res is ""
            for elem in level:
                if self.isValid(elem):
                    level_res.append(elem)
            
            # construct BFS levels (subtring that missing one char), each level could be the final res
            # by doing this, res.append(valid_elem), return the res once it is not null
            # this satisfy the question:
                  # 1, minimum removal
                  # 2, all possible results, at the same BFS level
            if level_res:
                return level_res
            
            next_level = set()
            for elem in level:
                for i in range(len(elem)):
                    next_level.add(elem[:i] + elem[i + 1:])
            
            level = next_level
            
    
    def isValid(self, s):
        balance = 0
        for ch in s:
            if balance < 0:
                return False
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
        
        return balance == 0
        
