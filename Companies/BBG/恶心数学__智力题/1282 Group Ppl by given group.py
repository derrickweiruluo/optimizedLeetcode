'''
# groupSizes, idx 代表人，nums[i] 代表所属于的组的size
# 返回他们的分组

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]


Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
'''



class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        counter = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            counter[size].append(i)
            
        res = []
        for size, lst in counter.items():
            for i in range(0, len(lst), size):
                # for a len of 6, i = 0 and 3
                # res.append(lst[0: 0 + 3]) and (lst[3: 3 + 3])
                res.append(lst[i : i + size])
        print(counter)
        return res