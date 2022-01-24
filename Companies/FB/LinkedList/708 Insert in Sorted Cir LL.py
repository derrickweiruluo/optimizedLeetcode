"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""



# Clarifications:
# 1.    Head could any node
# 2.    circular LinkedList
# 3.    insert into any valid posiiton (duogedaan)
# 4.    if input is None, return the newNode


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        newNode = Node(insertVal)
        
        if not head:  # 如果head 为 None，返回newNode
            newNode.next = newNode
            return newNode
        
        cur = head  # head可以是任意一点
        
        while True:
            # case1: within the middle
            if cur.val <= insertVal <= cur.next.val:
                break
                
            # case 2: within the circular wrap around position
            elif cur.val > cur.next.val and (insertVal >= cur.val or insertVal <= cur.next.val): 
                break
                
            # case 3 # 题目定义head可以是任意一点，所以会有上面两个check都不满足的情况 例如 3-4-1 插入2， 3 is head
            elif cur.next == head:  
                break
                
            cur = cur.next
        
        # print(cur.val)
        newNode.next = cur.next
        cur.next = newNode
        
        return head