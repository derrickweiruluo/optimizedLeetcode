"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:
n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106

#########思路：
slow, fast 同速，只是领先一个身位，
slow和fast分别跳位链接，完事之后slow.next --> fast_copy
"""

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
