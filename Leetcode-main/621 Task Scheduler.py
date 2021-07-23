class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
#         This is a math/analytical trick question
        
#         Steps: 
#         1. count the number of occurrences of each "task"
#         2. find the maxFreq
#         3. find the number of task that has maxFreq

#         4. Math problem then:
#             4.1 res = (maxFreq - 1) * (n + 1) + maxFreqCount
#             4.2 if len(tasks) > res: res = len(tasks)
        
        
        taskCounter = list(collections.Counter(tasks).values())
        
        maxFreq = max(taskCounter)
        maxFreqCount = taskCounter.count(maxFreq)
        
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxFreqCount)
