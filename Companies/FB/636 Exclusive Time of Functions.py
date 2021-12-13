'''
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

'''



'''
Constrinats:
No two start events will happen at the same timestamp.
No two end events will happen at the same timestamp.
Each function has an "end" log for each "start" log.
'''


# In a more conventional approach, let's look between adjacent events, with duration time - prev_time. If we started a function, and we have a function in the background, then it was running during this time. Otherwise, we ended the function that is most recent in our stack.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n
        stack = []
        prev = 0
        
        for log in logs:
            fcn_id, fcn_type, log_time = log.split(':')
            fcn_id, log_time = int(fcn_id), int(log_time)
            
            if fcn_type == 'start':
                if stack:
                    time_used = log_time - prev
                    res[stack[-1]] += time_used
                stack.append(fcn_id)
                prev = log_time
            else:
                time_used = log_time - prev + 1
                res[stack.pop()] += time_used
                prev = log_time + 1
        
        return res