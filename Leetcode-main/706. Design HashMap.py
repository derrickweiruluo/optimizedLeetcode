class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodeArray = [Node() for _ in range(1000)]
    
    def _hash(self, key):
        return key % len(self.nodeArray)
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashKey = self._hash(key)
        curr = self.nodeArray[hashKey]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashKey = self._hash(key)
        curr = self.nodeArray[hashKey]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = self._hash(key)
        curr = self.nodeArray[hashKey]
        while curr.next:
            if curr.next.key == key:
                to_be_removed = curr.next
                curr.next = to_be_removed.next
                to_be_removed = None
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
