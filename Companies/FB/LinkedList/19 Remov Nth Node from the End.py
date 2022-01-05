'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# 简单来说，题目问 移除倒数 第N个 Node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Withouy dummy

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        
        # 如果以移除头部
        # 例如 1-2-3-4-5, n=5, remove 5th from end: --> 2-3-4-5
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head


# n = 2, remove 2nd
# 1-2-3-4-5-6
# fast first move to 3, then slow start
# fast stop at 6, and slow stop at 4


#* -------------------------

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head
        
        fast = slow = dummy
        
        # 这道题关键在于用两个指针，且推断出要offset的距离，最好拿张纸画一画
        # Fast 存在的意义是让slow停在要被去除的node的前一个
        for i in range(n):
            fast = fast.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        # skip the target node
        slow.next = slow.next.next
        
        return dummy.next




'''
n ahead - AC in 48 ms

The standard solution, but without a dummy extra node. Instead, I simply handle the special case of removing the head right after the fast cursor got its head start.'''

