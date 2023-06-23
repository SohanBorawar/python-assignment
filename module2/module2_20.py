# a Python function that takes a list of words and returns the length of the longest one.

words = input("Enter a list of words, separated by spaces: ").split()

max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
print(max_length)