'''
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

## 删除node且input不提供head
'''

class Solution:
    def deleteNode(self, node):
        
        # It is guaranteed that the node to be deleted is not a tail node in the list.
        # 不在尾部意味着一定存在 node.next
        # 这只是一个function，"delete" node by:
            # 1. changing node.val to node.next.val
            # 2. then dereferencing by node.next = node.next.next
        node.val = node.next.val
        node.next = node.next.next