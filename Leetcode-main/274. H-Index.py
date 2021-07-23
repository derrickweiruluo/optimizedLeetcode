class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n-i:
                return n-i
        return 0

# n - index 保证了 len = 1 的情况下也能return出数值
# trick: len - i = 后面 len - i 个item的数量
