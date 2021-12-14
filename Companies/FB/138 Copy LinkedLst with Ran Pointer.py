


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        dummy = copy = Node(-1, head, None)
        
        while head:
            temp = head.next
            newNode = Node(head.val, None, head.random)
            head.next = copy.next = newNode
            head = temp
            copy = copy.next
        
        copy = dummy.next # reset to copy pointer from the end to the start(head)
        while copy:
            if copy.random:
                copy.random = copy.random.next # orginal node's next pointer has been set to its copy in the previous manipulation
            copy = copy.next
        
        return dummy.next


# using dictionary
class Solution1:
    def copyRandomList(self, head):
        if not head:
            return
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]