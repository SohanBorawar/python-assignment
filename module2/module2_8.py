# A program to print wheater the passed letter is a vowel or not 

print(">>>>>>> to check entered letter is vowel or not ")


s=input("enter a letter S:")
s=s.lower()
#print(s)

if len(s)<2 and len(s)>0:
    if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
        print("the enter letter is vowel")

    else :
        print("entered letter is not a vowel ")

else:
    print('invalid')