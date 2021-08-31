"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

EX: [1,2,3,4,5] --> [1,5,2,4,3]
EX: [1,2,3,4,5,6] --> [1,6,2,5,3,4]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        # STEP 1:: 先找中间点
        # 奇数len, [1,2,3,4,5] --> [1,2,3], [4,5], where 4 is slow.next
        # 偶数len, [1,2,3,4,5,6] --> [1,2,3], [4,5,6], where 4 is slow.next
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2:: 反转后半段，斩断第一段和第二段的联系
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        # slow.next = None
        
        # STEP 3:: 链表合并
        head1, head2 = head, prev
        while head1 and head2:
            head1_next = head1.next
            head2_next = head2.next
            
            head1.next = head2
            head1 = head1_next
            
            head2.next = head1
            head2 = head2_next
    
        
