'''
开一个4位的锁

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

'''




'''
N = 4 dials
A = 10 digits
D: size of the initial dead locks + invalid locks

Time Complexity: O(2 * N * A^N) == 8 * 10000
where, N is Number of dials (4 in our case)

Space(Huahua): O(10000 + D)

There are 10 x 10 x 10 x 10 possible combinations => 10^4 => A^N
For each combination, we are looping 4 times (which is N) and in each iteration, there are substring operations ( which is O(N) * constant) => O(4N*constant) => O(4N) => O(NN) => O(N^2)
Total complexity => A^N * N^2, plus D to create the hashset => N^2 * A^N + D


Space: O(A^N + D)
'''



class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)
        queue = collections.deque([(0, "0000")])
        
        if "0000" in dead: return -1
        
        while queue:
            steps, code = queue.popleft()
            if code == target:
                return steps
            
            for i in range(4):
                digit = int(code[i])
                for next_digit in (digit - 1) % 10, (digit + 1) % 10:
                    next_code = code[:i] + str(next_digit) + code[i + 1:]
                    if next_code not in dead:
                        dead.add(next_code)
                        queue.append((steps + 1, next_code))
                        
        
        return -1