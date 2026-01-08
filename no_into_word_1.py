nom=input('Enter a two digit number:') #input always returns a string
no=int(nom)
print('number is ',no)

first=no//10
last=no%10

print('first digit is ',first)
print('last digit is ',last)

word=['zero','one','two','three','four','five','six','seven','eight','nine']
print(word[first],' ',word[last])
