scoreboard = [83, 12, 57, 4, -96, 28, 71, 39, 65, 2, 90]
tot_run=0
count=0
for score in scoreboard:
    try:
        if score<0:
            raise ValueError
        tot_run=tot_run+score
        count+=1
    except ValueError:
        print("values error")
print(tot_run)
try:
    average=tot_run/count
except ZeroDivisionError:
    print("You cant not divide by zero")
else:
    print(f"average is {average}")