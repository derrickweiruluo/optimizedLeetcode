"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.
Return the minimum cost of deletions such that there are no two identical letters next to each other.
Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.


Example 1:
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:
Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:
Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").


Here we first initialise a result variable to finally return the answer and it is 0 at first.
Then we traverse through the string from the 1st index.
Whenever we found the consecutive characters equal , then
Update the result by adding the current result value and the min(cost[i], cost[i-1])

Update the cost[i] by compareing bw the maximum value of cost[i] and cost[i-1]

Finally return the result.
"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        res, prev = 0, cost[0]
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                res += min(prev, cost[i])
                prev = max(prev, cost[i])
            else:
                prev = cost[i]
        
        return res
