# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        leftHalf, rightHalf = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        
        return self.merge(leftHalf, rightHalf)
    
    def merge(self, left, right):
        # 有且只有一个 lists[ListNode] is empty
        if not left or not right:
            return left or right
        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(right.next, left)
            return right
