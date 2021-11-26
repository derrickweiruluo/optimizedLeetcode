'''
dict sorting, return max, etc

https://www.programiz.com/python-programming/methods/dictionary
'''
import collections
dict = {1:200, 2:400}
counter = collections.Counter()

maxValue = max(dict.values())
maxKey = max(dict)
print(maxKey, maxValue)
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



####### String -- Array conversion
A = [1,2,3,3,3,2,4]
cur = ''.join(map(str, A[0 : 3]))
print(cur)
int_arr = list(map(int, cur))
print(int_arr, 'This is an int array')



######## String 常用写法:
s = ''
s.isalpha()
s.isdigit()
s.isalnum()


###### Array copy 
# https://www.programiz.com/python-programming/shallow-deep-copy
cur = [1,24,5]
copy1 = cur[:]
copy2 = cur


copy1[0] = 999
print('cur', cur)
print('copy1', copy1)

copy2[0] = 100

print('cur', cur)
print('copy1', copy1)
print('copy2', copy2)

