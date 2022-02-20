'''
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
'''



# Time: O(n^2): We loop over people once, and each insertion is an O(n) operation. 
# Space O(n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        
        return res
    
# [[7,0]] (insert [7,0] at index 0)
# [[7,0],[7,1]] (insert [7,1] at index 1)
# [[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
# [[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
# [[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)