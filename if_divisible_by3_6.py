'''write a program to input number and check if 
number is divisible by 3 and 6 both then display it divisible by both number'''
nom=int(input("Enter number :"))
if nom%3==0 and nom%6==0:
    print("This number divisible by both number")
else:
    print('This number is not divisible by both number')
