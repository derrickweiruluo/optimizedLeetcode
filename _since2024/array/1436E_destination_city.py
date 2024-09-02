"""
Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(p[1] for p in paths) - set(p[0] for p in paths)).pop()


class Solution1_verbose_not_ideal:
    def destCity(self, paths: List[List[str]]) -> str:

        start_counter = collections.defaultdict(int)
        dest_counter = collections.defaultdict(int)
        for start, dest in paths:
            start_counter[start] += 1
            dest_counter[dest] += 1
        for k in dest_counter:
            if dest_counter[k] == 1 and start_counter[k] == 0:
                return k