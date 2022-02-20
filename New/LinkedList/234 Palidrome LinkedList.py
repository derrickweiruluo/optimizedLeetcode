

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # find the mid node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        #1->2->null :: 2->1->null
        tail = None
        while slow:
            slowNext = slow.next
            slow.next = tail
            tail = slow
            slow = slowNext
        # first break the mid, mid.next = null
        # then rotate the second half
        # 1->2->3 <-2<-1
            #   |
            #  null



        # compare the first and second half nodes
        # head 有可能比tail多一个node， 偶数的情况
        # 基数的话不会发生
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        
        return True
        