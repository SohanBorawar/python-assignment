# Write a Python program to count the frequency of words in a file.
file = open("mod2.txt","w")
file.write("hello hello this is second text file of the text file")
file.close()
print("*"*60)


with open("mod1.txt", 'r') as file:
    text = file.read()


words = text.split()


word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Print the word frequencies
for word, frequency in word_frequency.items():
    print(word_frequency)

    print(word, ':', frequency)
