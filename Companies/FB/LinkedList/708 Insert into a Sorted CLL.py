'''
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]



'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        newNode = Node(insertVal)
        
        if not head:
            newNode.next = newNode
            return newNode
        
        cur = head
        # Given a Circular Linked List node, which is sorted in ascending order
        
        while True:
            if cur.val <= insertVal <= cur.next.val:
                break
            elif cur.val > cur.next.val and (insertVal >= cur.val or insertVal <= cur.next.val):
                break
            elif cur.next == head:
                break
            cur = cur.next
        
        # print(cur.val)
        newNode.next = cur.next
        cur.next = newNode
        
        return head