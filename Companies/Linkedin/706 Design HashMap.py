

class Node:
    
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.arr = [Node() for _ in range(10000)]
        self.n = 10000
        
    def _hash(self, key):
        return key % self.n

    def put(self, key: int, value: int) -> None:
        hKey = self._hash(key)
        cur = self.arr[hKey]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return None
            cur = cur.next
        cur.next = Node(key, value)
        
    def get(self, key: int) -> int:
        hKey = self._hash(key)
        cur = self.arr[hKey]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hKey = self._hash(key)
        cur = self.arr[hKey]
        while cur.next:
            if cur.next.key == key:
                to_be_removed = cur.next
                cur.next = cur.next.next
                to_be_removed = None
                return None
            cur = cur.next
        return None 

