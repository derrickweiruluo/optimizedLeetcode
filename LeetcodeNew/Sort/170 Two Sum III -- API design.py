'''
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

'''

class TwoSum:

    def __init__(self):
        self.arr = []
        self.counter = collections.Counter()

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.counter[number] += 1
        
    def find(self, value: int) -> bool:
        for num in self.arr:
            if (value - num) in self.counter:
                if num * 2 != value or self.counter[num] > 1:
                    return True
        return False
        