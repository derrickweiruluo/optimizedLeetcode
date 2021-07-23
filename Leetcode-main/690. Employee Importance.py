"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emps = {employee.id: employee for employee in employees}

        def dfs(emp_id):
            sub_importance = sum(dfs(sub_id) for sub_id in emps[emp_id].subordinates)
            return emps[emp_id].importance + sub_importance
        
        return dfs(id)
