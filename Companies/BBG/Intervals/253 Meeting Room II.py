'''
给一串会议时间，问需要多少个房间
'''
class Solution:  # 最优解 O(nlogn + n), space O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        lst = []
        for interval in intervals:
            lst.append((interval[0], 1))  # start time
            lst.append((interval[1], -1)) # end time
        
        lst.sort()

        res = count = 0
        for point in lst:
            count += point[1]
            res = max(res, count)
        
        return res




# Time: O(nlogn) * 2, Space O(n), if the min-heap has every meeting room
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        heap = [intervals[0][1]]  # heap of earliest-finished meeting
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappushpop(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        
        return len(heap)



### FOLLOW UP t
# This question has its follow-up as asking you to output the meeing schedule for each room. I have seen people mentioned the follow-up in Google and FB interviews.
# Basically we need to keep track of which room is empty when we pop from the priority_queue: 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 
        intervals.sort(key = lambda x: (x[0], x[1]))
        heap = []
        res = []
        
        for i in range(len(intervals)):
            roomId = i
            if heap and intervals[i][0] >= heap[0][0]:
                roomId = heap[-1][1]
                heapq.heappushpop(heap, (intervals[i][1], roomId))
            else:
                roomId = len(heap)
                res.append([])
                heapq.heappush(heap, (intervals[i][1], roomId))
            res[roomId].append(intervals[i])
        
        print(res)
        return len(heap)




class Solution3:  # sort + two pointers
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 01/12/22 with follow ups https://leetcode.com/submissions/detail/618754331/
        # 数飞机 https://leetcode.com/submissions/detail/619997197/
        
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        
        starts.sort()
        ends.sort()
        
        j = 0   # right pointer
        res = 0
        for i in range(len(starts)):
            if starts[i] < ends[j]:
                res += 1
            else:
                j += 1
        
        return res





# if input is small:

'''
class Solution {
public:
int minMeetingRooms(vector<vector<int>>& intervals) {
        vector<int> arr(1000000,0);
        for(int i=0;i<intervals.size();i++){
            arr[intervals[i][0]]++;
            arr[intervals[i][1]]--;
            
        }
        int mx=0,sum=0;
        for(int i=0;i<arr.size();i++)
        {
            sum+=arr[i];
            mx=max(mx,sum);
        }
        return mx;
    }
};
'''