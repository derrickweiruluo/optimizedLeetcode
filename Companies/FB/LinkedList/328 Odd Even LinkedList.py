'''
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        
        slow, fast = head, head.next
        fast_copy = fast
        # slow, fast 同速，只是领先一个身位，slow和fast分别跳位链接，完事之后slow.next --> fast_copy
        while fast and fast.next:
            slow.next = slow.next.next
            fast.next = fast.next.next
            slow = slow.next
            fast = fast.next
        
        slow.next = fast_copy
        
        return head