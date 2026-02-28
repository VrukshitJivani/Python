#custome exceptions
class voteAgeException(Exception):
    pass

age=int(input("Enter Age:"))
try:
    if age<18:
        raise voteAgeException("You are not aligible for vote ")
except voteAgeException as error:
    print(error)
else:
    print("You are aligible for vote")