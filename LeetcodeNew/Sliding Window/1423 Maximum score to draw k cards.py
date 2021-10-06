'''
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards. Your score is the sum of the points of the cards you have taken. Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Ex 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12

Ex 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55

Ex 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1

Ex 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202

'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        score = sum(cardPoints[:k])
        res = score
        for i in range(1, k + 1):
            score += (cardPoints[-i] - cardPoints[k - i])
            res = max(res, score)
        
        return res
    
#     [1, 2, 3, 4, 5, 6, 1]
#     [1, 2, 3] +       []
#     [1, 2] +          [1]
#     [1] +             [6, 1]
#     [] +              [5, 6, 1]
    