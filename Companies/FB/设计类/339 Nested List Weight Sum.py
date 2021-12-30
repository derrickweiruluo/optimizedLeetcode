'''
Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.


Example 2:

Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

'''

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def bfs(nestedList, level):
            res = 0
            innerList = []
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger() * level
                else:
                    innerList.extend(item.getList())
            if innerList:
                res += bfs(innerList, level + 1)
            return res
        
        return bfs(nestedList, 1)