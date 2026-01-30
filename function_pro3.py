"""write a program to create function 
that convert given fahrenheit 
into celsius(32°F − 32) × 5/9 = 0°C
""" 

def conCelsius(tem):
    cel=(tem-32)*5/9
    return cel
    
fah=int(input("Enter Fahrenheit :"))
ans=conCelsius(fah)   
print(" Fehrenheit is ",ans)