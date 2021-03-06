# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# O (nlogK)
# O (k + n), k for heap and n for creating new LL

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = [(head.val, idx, head) for idx, head in enumerate(lists) if head]
        heapq.heapify(heap)  # using (val, idx, head) tuple is for python to compare if node.val is the same 
        root = cur = ListNode()
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
        
        return root.next


#*--------------------------------

# Divide and Conquer
# O (nlogK)
# O(logK), 8个LL的话，只需要 log8次 merge， 每一次merge耗费O(n), n 是两个LL的node数量


# Suppose initially each list is of average length n, then:
# k/2*(2n) + k/4*(4n) + k/8*(8n)... + = logk * (kn)

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





class Solution:  # Heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = [(head.val, idx, head) for idx, head in enumerate(lists) if head]
        heapq.heapify(heap)  # # using (val, idx, head) tuple is for python to compare if node.val is the same 
        root = cur = ListNode()
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
        
        return root.next
        