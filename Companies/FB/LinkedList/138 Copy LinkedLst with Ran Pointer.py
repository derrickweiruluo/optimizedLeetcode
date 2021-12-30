'''
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 思路：
# 1.    在现有的LL上面构建一个copy LL（random pointer也复制一份）
# 2.    并且每一个新的copy node构建完以后，original的next被改成copyNode，方便copy1 通过 original's random 的 next 找到对应的 copynode

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





#-----------------
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