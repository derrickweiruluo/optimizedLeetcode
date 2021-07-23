class Solution:
    #def oddEvenJumps(self, arr: List[int]) -> int:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1
        for i in range(n - 1)[::-1]:  #这一步开始不懂
            odd[i] = even[next_higher[i]]
            even[i] = odd[next_lower[i]]
        # print(next_higher)
        # print(next_lower)
        # print(higher)
        # print(lower)
        return sum(odd)
