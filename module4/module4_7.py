# Write a python program to find the longest words.

with open("mod1.txt", 'r') as file:
    text = file.read()
    
words = text.split()
print(words)
longest_length = max(len(word) for word in words)
print(longest_length)
longest_words = [word for word in words if len(word) == longest_length]

print("Longest word(s):", longest_words)



'''
with open("mod1.txt","r") as file:
    r = file.read()
text = r.split()
print(text)
leng = 0

for i in text:
    if len(i) > leng:
        leng = len(i)
        word = i
print(word)   
print(leng)  '''
