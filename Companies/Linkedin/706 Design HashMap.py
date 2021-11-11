

class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.nodeArr = [Node() for _ in range(1000)]
        self.n = 1000
        
    def hash(self, key):
        return key % self.n

    def put(self, key: int, value: int) -> None:
        hKey = self.hash(key)
        cur = self.nodeArr[hKey]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)  # if the key not used, create a new node at the end

    def get(self, key: int) -> int:
        hKey = self.hash(key)
        cur = self.nodeArr[hKey]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hKey = self.hash(key)
        cur = self.nodeArr[hKey]
        while cur.next:
            if cur.next.key == key:
                to_be_removed = cur.next
                cur.next = to_be_removed.next
                to_be_removed = None
                return
            cur = cur.next
        return 

