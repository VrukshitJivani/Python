hour=int(input("Enter hour:"))

if hour>=1 and hour<=12:
    print(f'hour is {hour} AM')


if hour>=13 and hour<25:
    per_hour=hour-12
    print(f'hour is {per_hour} PM')


if hour>24:
    print("Invalide hour")