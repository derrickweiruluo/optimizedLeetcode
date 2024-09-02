"""
The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # The lock initially starts at '0000', a string
        # representing the state of the 4 wheels.
        deadends = set(deadends)
        queue = collections.deque([("0000", 0)])

        if "0000" in deadends:
            return -1

        while queue:
            current_try, count = queue.popleft()
            if current_try == target:
                return count
            for i in range(4):
                current_digit = int(current_try[i])
                for next_digit in (current_digit - 1) % 10, (current_digit + 1) % 10:
                    next_try = current_try[:i] + str(next_digit) + current_try[i + 1:]
                    if next_try not in deadends:
                        deadends.add(next_try)
                        queue.append((next_try, count + 1))

        return -1
