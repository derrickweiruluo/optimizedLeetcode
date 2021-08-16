"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

EX1:
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.


###########
https://leetcode.com/problems/cinema-seat-allocation/
https://leetcode.com/problems/cinema-seat-allocation/discuss/552211/Python-Very-concise-solution-using-hash-map

We use three numbers to record whether the left, the middle or the right is occupied or not.
First, we record whether the left, middle or right is occupied or not using a set as the value in the dictionary.
For n rows, the maximum number of families that can sit together are 2*n.
Then we iterate through the dictionary, if all three positions in the row was blocked, the total cnt should -2.
If less than 3 positions was blocked, the total cnt should -1.
"""

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        seated = collections.defaultdict(set)
        for i, j in reservedSeats:
            if j in [2,3,4,5]:
                seated[i].add(0)
            if j in [4,5,6,7]:
                seated[i].add(1)
            if j in [6,7,8,9]:
                seated[i].add(2)
        
        res = 2 * n
        for i in seated:
            if len(seated[i]) == 3:
                res -= 2
            else:
                res -= 1
        
        return res
