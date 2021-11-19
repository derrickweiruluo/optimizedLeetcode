'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
'''

'''
https://youtu.be/wYqLisoH80w?t=434

'''

import collections
class Node:
    
    def __init__(self, val, prev = None, next = None):
        self.val = val      # counter of frequency 
        self.prev = prev
        self.next = next
        self.keys = set()   # a set of keys @ this frequency

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        # {frequency: node}, where each node stores a set of strings
        self.mapping = collections.defaultdict(lambda: self.head) # frequency default to be 0

    def inc(self, key: str) -> None:
        # 每次inc/dec 操作，都要先提取该node，然后断掉mapping[key]
        cur = self.mapping[key]
        cur.keys.discard(key)
        self.mapping.pop(key)
        
        if cur.val + 1 == cur.next.val:
            curNext = cur.next
        else:
            curNext = Node(cur.val + 1, cur, cur.next)
            curNext.prev.next = curNext
            curNext.next.prev = curNext
        
        curNext.keys.add(key)
        self.mapping[key] = curNext
        
        # 如果该node 没 keys了 且这不是head/tail node，就在双linkedList里面skip掉
        # 指针指向 next.next and prev.prev
        if not cur.keys and cur.val != 0:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def dec(self, key: str) -> None:
        if not key in self.mapping: return
        # 每次inc/dec 操作，都要先提取该node，然后断掉mapping[key]
        cur = self.mapping[key]
        cur.keys.discard(key)
        self.mapping.pop(key)
        
        if cur.val > 1:
            if cur.val - 1 == cur.prev.val:
                curPrev = cur.prev
            else:
                curPrev = Node(cur.val - 1, cur.prev, cur)
                curPrev.prev.next = curPrev
                curPrev.next.prev = curPrev

            curPrev.keys.add(key)
            self.mapping[key] = curPrev
        
        # 如果该node 没 keys了 且这不是head/tail node，就在双linkedList里面skip掉
        # 指针指向 next.next and prev.prev
        if not cur.keys and cur.val != 0:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def getMaxKey(self) -> str:
        if self.tail.prev.val == 0: return ''   # tail.prev is the maxFreq IF tail.prev != head
        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.head.next.val == 0: return ''   # head.next is the minFreq IF head.next != tail
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key