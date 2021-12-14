"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

# Deque and HashMap, deque.remove() is O(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.deque = collections.deque([])
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.deque.remove(key)  # O(1) deque is DLL implemented
        self.deque.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deque.remove(key)
        elif len(self.cache) == self.capacity:
            val = self.deque.popleft()
            self.cache.pop(val)
        self.deque.append(key)
        self.cache[key] = value


### BAD, orderdict should not used
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.key_dict:
            return -1
        self.key_dict.move_to_end(key, last = True)
        return self.key_dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_dict:
            self.key_dict.move_to_end(key, last = True)
        self.key_dict[key] = value
        if len(self.key_dict) > self.capacity:
            self.key_dict.popitem(last = False)
