'''
dict sorting, return max, etc


https://www.programiz.com/python-programming/methods/dictionary
'''

dict = {1:200, 2:400}

returnMaxValue = max(dict.values())
returnMaxKey   = max(dict, dict.keys())
returnMaxKey   = max(dict, key=dict.get)

print(dict.keys(), dict.values())


dict = {0:100, 20:100, 3:100, 2:100}
sorting = sorted(dict.items(), key = lambda x: (x[1], x[0]))


