#logical operator
# and or not
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
#12,34
a=num1==num2 and num1<num2
print(a)

b=num1==num2 or num1<num2
print(f"{b}={num1}=={num2} or {num1}<{num2}")

c=not(num1==num2 and num1<num2)
print(f"{c}=not({num1}=={num2} and {num1}<{num2})")
