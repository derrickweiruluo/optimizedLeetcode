
'''
NOTE for 最优解 N/A for Python
Using structures like Array or Stack will never let us popMax quickly. We turn our attention to tree and linked-list structures that have a lower time complexity for removal, with the aim of making popMax faster than O(N)O(N) time complexity.

Say we have a double linked list as our "stack". This reduces the problem to finding which node to remove, since we can remove nodes in O(1)O(1) time.

We can use a TreeMap mapping values to a list of nodes to answer this question. TreeMap can find the largest value, insert values, and delete values, all in O(\log N)O(logN) time.

'''



# https://leetcode.com/problems/max-stack/discuss/1373061/Python-pure-TreeMap-Solution-with-detailed-explanation
from sortedcontainers import SortedDict

class Node:
    
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MaxStack:

    def __init__(self):
        self.head = Node()
        self.tail = Node(prev = self.head)
        self.head.next = self.tail
        self.sortedDict = SortedDict()
        
    def push(self, x: int) -> None: # O(log(n))
        newNode = Node(x)
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        newNode.next = self.tail
        self.tail.prev = newNode
        
        if x not in self.sortedDict:
            self.sortedDict[x] = [newNode]
        else:
            self.sortedDict[x].append(newNode)

    def pop(self) -> int: # O(log(n))
        removedNode = self.tail.prev
        removedNode.prev.next = self.tail
        self.tail.prev = removedNode.prev
        
        self.sortedDict[removedNode.val].pop()
        if not self.sortedDict[removedNode.val]:
            del self.sortedDict[removedNode.val]
        return removedNode.val

    def top(self) -> int: # O(1)
        return self.tail.prev.val

    def peekMax(self) -> int: # O(log(n))
        return self.sortedDict.peekitem()[0]

    def popMax(self) -> int: # O(log(n))
        maxVal = self.peekMax()
        removedNode = self.sortedDict[maxVal].pop()
        removedNode.prev.next, removedNode.next.prev = removedNode.next, removedNode.prev
        
        if not self.sortedDict[maxVal]:
            del self.sortedDict[maxVal]
        return maxVal








# https://leetcode.com/submissions/detail/583091722/
# https://leetcode.com/submissions/detail/595120631/

# This solution

# import collections, heapq
# https://leetcode.com/problems/max-stack/discuss/1003655/Python-O(logN)-use-double-linked-list-%2B-heap-%2B-dictionary
#Java TreeMap
# https://leetcode.com/problems/max-stack/discuss/129922/Java-simple-solution-with-strict-O(logN)-push()popMax()pop()
class MaxStack:  # not thie one

    def __init__(self):
        # stack of [(cur_Val, maxIdx)]
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            idx = len(self.stack)
        else:
            if self.stack:
                idx = self.stack[-1][1]
            else:
                idx = 0
        self.stack.append((x, idx))
    
    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]        

    def popMax(self) -> int:
        maxIdx = self.stack[-1][1]
        res = self.stack[maxIdx][0]
        nextMax = self.stack[self.stack[maxIdx - 1][1]][0] if maxIdx != 0 else -math.inf
        for i in range(maxIdx, len(self.stack) - 1):
            if self.stack[i + 1][0] >= nextMax:
                nextMax = self.stack[i + 1][0]
                self.stack[i] = (self.stack[i + 1][0], i)
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])
        self.stack.pop()
        return res