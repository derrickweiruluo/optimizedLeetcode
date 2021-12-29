'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

'''

# Naive sol
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter()
        for w in words:
            counter[w] += 1
        
        # sorting condition 1: -counter[x], which sort the most negative frequency, the most frequent
        # sorting condition 2: if there is a tie, sort by lower lexicographical order
        return sorted(counter, key = lambda x: (-counter[x], x))[:k]