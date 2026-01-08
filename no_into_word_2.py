nom=input("Enter a three digit number:")
no=int(nom)
print('number is ',no)
#no is 123
first=no//100
print(first)#1

middle=(no//10)%10
print(middle)#2

last=no%10
print(last)#3

list1=['zero','one','two','three','four','five','six','seven','eight','nine']

print(list1[first],list1[middle],list1[last])
#one two three