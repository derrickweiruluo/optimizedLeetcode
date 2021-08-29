"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?

#######
思路：
把cur 定位到left node
然后 对掉 in range(right - left)次
最好手动画一下
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(-501, head)
        
        prev, cur = dummy, head
        
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
        
        for _ in range(right - left):
            # 手动对掉下
            cur_next = cur.next
            cur.next = cur_next.next
            cur_next.next = prev.next
            prev.next = cur_next
        
        return dummy.next
            
        
