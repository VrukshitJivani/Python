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
        print("In list values is not valide")
print(tot_run)
try:
    average=tot_run/count
except ZeroDivisionError:
    print("All value are invalide ,so average is not generate ")
else:
    print(f"Average is {average}")
