# sum of elements in list 

l = [556,755,161,156,111,489,753,456,123,332,121,147,254]

sum = 0
larger = 0

print(len(l))
#l.sort()
#print
# (l)

for i in l:
    sum = sum + i
print(sum)

for j in l:
    if larger < j:
        larger = j
print(larger)

smaller = larger

for k in l:
    if smaller > k:
        smaller = k
print(smaller)
