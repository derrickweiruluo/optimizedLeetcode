'''
Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

'''



from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_dict = {}
        self.freq_dict = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_dict:
            return -1
        freq = self.key_dict[key]
        val = self.freq_dict[freq][key]
        del   self.freq_dict[freq][key]
        if not self.freq_dict[freq]:
            if freq == self.min_freq:
                self.min_freq += 1
            del self.freq_dict[freq]
        new_freq = freq + 1
        self.key_dict[key] = new_freq
        self.freq_dict[new_freq][key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity < 1:
            return
        if key in self.key_dict:
            freq = self.key_dict[key]
            self.freq_dict[freq][key] = value
            self.get(key)
        else:
            if len(self.key_dict) == self.capacity:
                del_key, del_val = self.freq_dict[self.min_freq].popitem(last = False)
                del self.key_dict[del_key]
            self.key_dict[key] = 1
            self.freq_dict[1][key] = value
            self.min_freq = 1


#*-------------------------------------

import collections

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        if not node:
            node = self._sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node
        
class LFUCache:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._node = dict() # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0
        
        
    def _update(self, node):
        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1