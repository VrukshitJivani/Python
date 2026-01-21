"""Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------"""

sub_mark1=int(input("Enter first subject marks :"))
sub_mark2=int(input("Enter second subject marks :"))
sub_mark3=int(input("Enter third subject marks :"))
sub_mark4=int(input("Enter fourth subject marks :"))
sub_mark5=int(input("Enter fifth subject marks :"))

tot=sub_mark1+sub_mark2+sub_mark3+sub_mark4+sub_mark5
per=tot/5

print(f"Total is {tot}")
print(f"Percentage is {per}")

if per>=90 and per<=100:
    print("Grade : A+")
elif per>=80 and per<90:
    print("Grade : A")
elif per>=70 and per<80:
    print("Grade : B")
elif per>=60 and per<70:
    print("Grade : C")
elif per>=50 and per<60:
    print("Grade : D")
else:
    print("Need Improvement")
