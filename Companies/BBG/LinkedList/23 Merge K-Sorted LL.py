'''
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

import heapq

# Merge Sort
# Time O(Nlogk), N is the total nodes in final LL, n is nodes in each LL
# Time O(nk*log(k))
# N = n*k
# Space O(logk)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        if l1.val >= l2.val:
            l2.next = self.merge(l2.next, l1)
            return l2


'''
merge([1,4,5], merge([1,3,4], [2,6])):
[1,3,4], [2,6]
    1 ->merge([3,4], [2,6])
    1 -> 2 -> [3,4], [6]
    [1,2,3,4,6]

merge([1,4,5], [1,2,3,4,6])
    [1,1,2,3,4,4,5,6]'''



# Time: O(Nlogk) where k is the number of linked lists., N is the final amount of nodes
# Space: O(n) for creating new LL, O(k) for heap
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        heap = [(head.val, idx, head) for idx, head in enumerate(lists) if head]
        heapq.heapify(heap)
        root = cur = ListNode()
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
        
        return root.next





# Time complexity: O(nk)
# Space complexity: O(1)

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next