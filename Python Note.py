'''
dict sorting, return max, etc


https://www.programiz.com/python-programming/methods/dictionary
'''
import collections
dict = {1:200, 2:400}
counter = collections.Counter()

maxValue = max(dict.values())
maxKey   = max(dict, dict.keys())
maxKey   = max(dict, key=dict.get)
maxKey   = max(d.keys())
counter.elements()

print(dict.keys(), dict.values())


dict = {0:100, 20:100, 3:100, 2:100}
sorting = sorted(dict.items(), key = lambda x: (x[1], x[0]))


######  旋转2D array 顺时针 90
A = [[1,2,3],[4,5,6],[7,8,9]]
A1 = [[1,2,3],[4,5,6],[7,8,9]]
print(A)
for i in range(times):
    A = [[row[i] for row in A[::-1]] for i in range(len(A))]
    A1 = [list(col)[::-1] for col in zip(*A1)]

print(A)
print(A1)
