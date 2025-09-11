from typing import List
import itertools

# 1. Factorial (recursion + iteration).

class Factorial:

    def fact(self,number:int)->int:
        factorial = 1
        if number == 0:
            return 1
        else:
            return number * self.fact(number-1)

obj = Factorial()
print(obj.fact(6))

# 2. Flatten a nested list.

def flatten(array):
    flat = list(itertools.chain.from_iterable(array))
    return flat

print(flatten([[4,5],[1,2,3,4,7]]))
