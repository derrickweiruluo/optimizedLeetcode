# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Time complexity : 
O(N log K )
N is the number of nodes in two lists
K is the number linkedLists

O(1) Space
'''


# Divide and Conquer
# O (NlogK)
# O(logK), 8个LL的话，只需要 log8次 merge， 每一次merge耗费O(N), N 是两个LL的node数量
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        # divide and conquer 到单链，然后merge，把merge的结果递归结果到上一层
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        


        return self.merge(left, right)
    
    def merge(self, l1, l2): # O(N)
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l2.next, l1)
            return l2
