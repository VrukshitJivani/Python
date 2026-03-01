class InvalidMarksError(Exception):
    pass

marks = int(input("Enter marks: "))

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Marks accepted:", marks)
except InvalidMarksError as e:
    print("Error:", e)