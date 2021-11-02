'''
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8



Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
'''

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        def bfs(nestedList, curSum):
            innerList = []
            for item in nestedList:
                if item.isInteger():
                    curSum += item.getInteger()
                else:
                    innerList.extend(item.getList())
            if innerList:
                curSum += bfs(innerList, curSum)
            return curSum
        
        return bfs(nestedList, 0)