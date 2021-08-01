class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n  # total of n function calls
        stack = []
        prev_time = 0
        
        # logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}"
        # log time is in chronological order
        # treat each time[i] as a time interval, not as a point
        
        for log in logs:
            fcn_id, fcn_type, log_time = log.split(":")
            fcn_id, log_time = int(fcn_id), int(log_time)
            
            if fcn_type == "start":
                if stack:
                    time_used = log_time - prev_time # diff of two start times
                    res[stack[-1]] += time_used
                stack.append(fcn_id)
                prev_time = log_time
            else:
                time_used = log_time - prev_time + 1
                res[stack.pop()] += time_used
                prev_time = log_time + 1 # because log_time is already used
            
            
        return res
