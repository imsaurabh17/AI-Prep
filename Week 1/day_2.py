from typing import List

# 1. Print Fibonacci sequence up to N.
class Fibonacci:

    def __init__(self,number:int):
        self.n = number

    def fib_seq(self)->List[int]:
        seq = []
        for i in range(0,self.n):
            if len(seq)<2:
                seq.append(i)
            else:
                seq.append(seq[i-1]+seq[i-2])
        print(seq)

obj = Fibonacci(10)

obj.fib_seq()


# 2. Find all even numbers in a list using comprehension.

class Even:

    def __init__(self,numbers:List[int]):
        self.arr = numbers

    def even(self):
        print([num for num in self.arr if (num%2==0)])

obj = Even([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

obj.even()
