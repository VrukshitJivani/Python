#Exception Handling with list 
score = ["Virat Kohli", 78, "Rohit Sharma", 92, "MS Dhoni", 65, "KL Rahul", 81, "Hardik Pandya", 74,12,78,65,34]
tot_score=0
for i in score:
    try:
        tot_score=tot_score+i
    except TypeError:
        print(f"{i} Values is invalide so it is skiped")
print(f"Total run is {tot_score}")