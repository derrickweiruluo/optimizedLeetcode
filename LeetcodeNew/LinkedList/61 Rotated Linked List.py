'''
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return None
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        k = k % length
        cur.next = head
        
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        res = temp.next
        temp.next = None
        return res