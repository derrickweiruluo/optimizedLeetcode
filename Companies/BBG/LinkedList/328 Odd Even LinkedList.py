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
        
        # slow, fast 同速，只是领先一个身位，slow和fast分别跳位链接，完事之后slow.next --> fast_copys
        slow, fast = head, head.next
        fastStart = fast
        
        
        while fast and fast.next:
            
            # 坑, 一定要先挪 slow， 先挪fast 会 印象slow
            # 因为 fast.next 是 slow要跳到的地方
            slow.next = slow.next.next  # jump one node and connenct even --> even
            fast.next = fast.next.next  # jump one node and connenct odd-->odd
            
            slow = slow.next # advance to next node
            fast = fast.next
        
        slow.next = fastStart  # connect the end node of slow to Fast
        return head