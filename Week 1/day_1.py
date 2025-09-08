# 1) Reverse a string without using [::-1].

class ReverseString:

    def __init__(self,string:str):
        self.string = string

    def reverse(self)->str:
        new = ""
        for i in range(len(self.string)-1,-1,-1):
            new += self.string[i]
        print(f"The reverse of {self.string} is {new}")

obj = ReverseString("Hi how are you?")
obj.reverse()

# 2) Count frequency of words in a sentence.

class Count:

    def __init__(self,sentence:str,target:str):
        self.sentence = sentence
        self.target = target

    def word_count(self)->int:
        counter = 0
        for i in self.sentence.split():
            if i == self.target:
                counter += 1
        print(f"The {self.target} is repeated {counter} times in the provided sentence")

obj = Count("my name is saurabh and your name is xyz.","name")
obj.word_count()