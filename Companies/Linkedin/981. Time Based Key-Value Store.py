'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


'''

# https://leetcode.com/problems/time-based-key-value-store/discuss/408651/Python-clean-solution-binary-search
# https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/
# https://leetcode.com/submissions/detail/585690308/

class TimeMap:

    def __init__(self):
        self.memo = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""
        data = self.memo[key]
        left, right = 0, len(data)
        while left < right:
            mid = (left + right) // 2
            if data[mid][1] > timestamp:
                right = mid
            else:
                left = mid + 1
                
        if data[left - 1][1] > timestamp: return ""
        return data[left - 1][0]
        
        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)