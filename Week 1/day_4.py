# 1. Read a text file and count unique words.

word_to_count = 'list'
counter = 0
with open("day_1.txt","r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word == word_to_count:
                counter += 1
print(f"The {word_to_count} is repeated {counter} times in day_1.txt file")


# 2. Handle division by zero safely.

try:
    a,b = map(int,input("Enter two numbers: ").split())
    print(a/b)
except ZeroDivisionError:
    print("Denominator can not be zero")