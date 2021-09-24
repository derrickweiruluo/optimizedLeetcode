'''
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]

Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]



#########
https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

Whenever the CPU is not busy we always want to give it the shortest task.
This is a solid hint that we should be thinking about a min heap because it will
always have the smallest (shortest) item at position 0.

Remember to check if the heap is empty before trying to pop from it.
If it is empty, then let the CPU sit idle.
This just means increase the time to when the next task can be pushed into the heap.

'''


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        res = []
        # sort the task by enqueueTime, processTime and idx, idx is used when there is a tie
        tasks = sorted([(t[0], t[1], idx) for idx, t in enumerate(tasks)], key = lambda x: (x[0], x[1], x[2]))
        tasksHeap = []
        cur_time = tasks[0][0]
        idx = 0
        taskCount = len(tasks)
        
        while len(res) < taskCount:
            while idx < taskCount and tasks[idx][0] <= cur_time:
                heapq.heappush(tasksHeap, (tasks[idx][1], tasks[idx][2]))  # heap of (processTime, idx)
                idx += 1
            if tasksHeap:  # can only handle one task at a time
                processTime, taskIdx = heapq.heappop(tasksHeap)
                res.append(taskIdx)
                cur_time += processTime
            elif idx < taskCount: # if idle, fastforward to the next task
                cur_time = tasks[idx][0]
        
        return res
