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


当被问到clost left to target, which is right bound
同样的template，被改只有 when arr[mid] <= target: left = mid + 1
&& return left - 1
"""

class TimeMap:

    def __init__(self):
        self.timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps timestamp of set are strictly increasing.
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ''
        data = self.timestamps[key]
        left, right = 0, len(data)
        while left < right:
            mid = (left + right) // 2
            if data[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        
        if left == 0:  # 所有data的时间都 > timestamp
            return ''
        # left bound题 ，因为题目问 search res <= target
        return data[left - 1][1]
        
        '''
        Returns a value such that set was called previously, with timestamp_prev <= timestamp
        print(left, right)
        left == right and since it is moved to right when <= target, therefore need to return left - 1 or right - 1
        since it is asked for closest left, if left and right == 0, means all vals in arr is > target, therefore return ""
        '''

