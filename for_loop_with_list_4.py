#for loop with string
# count vowels  
name=input("Enter your name :")
vowels=['a','e','i','o','u']
v=0
for i in name:
    if str.lower(i) in vowels:
        v+=1
print("In this name vowel count is ",v)