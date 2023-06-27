# Write a Python script to check if a given key already exists in a dictionary.

d = {'a': 8, 'b': 2, 'c': 15, 'd': 1, 'e': 7}

k = input("enter the key :")

for i in d:
    if i==k:
        print("the key exist")
        break
    else:
        print("the key doesn't exist")   