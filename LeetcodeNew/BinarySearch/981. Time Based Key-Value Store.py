"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

#####
https://leetcode.com/problems/time-based-key-value-store/

Bisect_Right, Right Bound, 

"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        if not arr: return ""
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid
        
        return arr[left][1] if arr[left][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
