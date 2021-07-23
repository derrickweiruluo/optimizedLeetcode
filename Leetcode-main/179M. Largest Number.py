class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        compare = lambda a, b: 1 if a + b > b + a else -1 if a + b < b+ a else 0
        str_nums = sorted(map(str, nums), key = cmp_to_key(compare), reverse = True)
        return str(int("".join(str_nums)))

# sort in python, 
#   lambda function, named compared
# map(str, nums), convert int array "nums" to str array
# sorted(map(str, nums), key = cmp_to_key(compare), reverse = True)
