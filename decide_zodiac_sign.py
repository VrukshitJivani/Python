"""write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20
"""
man_birth_day=int(input("Enter Man Birth day :"))
man_birth_month=int(input("Enter Man Birth Month :"))

woman_birth_day=int(input("Enter Woman Birth day :"))
woman_birth_month=int(input("Enter Woman Birth Month :"))
man_zodic=None
woman_zodic=None


# Zodiac elements
fire = ["Aries", "Leo", "Sagittarius"]
earth = ["Taurus", "Virgo", "Capricorn"]
air = ["Gemini", "Libra", "Aquarius"]
water = ["Cancer", "Scorpio", "Pisces"]


#man

if (man_birth_month==3 and (man_birth_day>=21 and man_birth_day<=31)) or (man_birth_month==4 and (man_birth_day>=1 and man_birth_day<=19)):
    man_zodic="Aries"
    
elif (man_birth_month==4 and (man_birth_day>=20 and man_birth_day<=30)) or (man_birth_month==5 and (man_birth_day>=1 and man_birth_day<=20)):
    man_zodic="Taurus"
    
elif (man_birth_month==5 and (man_birth_day>=21 and man_birth_day<=31)) or (man_birth_month==6 and (man_birth_day>=1 and man_birth_day<=21)):
    man_zodic="Gemini"
    
elif (man_birth_month==6 and (man_birth_day>=22 and man_birth_day<=30)) or (man_birth_month==7 and (man_birth_day>=1 and man_birth_day<=22)):
    man_zodic="Cancer"

elif (man_birth_month==7 and (man_birth_day>=23 and man_birth_day<=31)) or (man_birth_month==8 and (man_birth_day>=1 and man_birth_day<=22)):
    man_zodic="Leo"

elif (man_birth_month==8 and (man_birth_day>=23 and man_birth_day<=31)) or (man_birth_month==9 and (man_birth_day>=1 and man_birth_day<=22)):
    man_zodic="Virgo"

elif (man_birth_month==9 and (man_birth_day>=23 and man_birth_day<=30)) or (man_birth_month==10 and (man_birth_day>=1 and man_birth_day<=22)):
    man_zodic="Libra"

elif (man_birth_month==10 and (man_birth_day>=24 and man_birth_day<=31)) or (man_birth_month==11 and (man_birth_day>=1 and man_birth_day<=21)):
    man_zodic="Scorpio"

elif (man_birth_month==11 and (man_birth_day>=22 and man_birth_day<=30)) or (man_birth_month==12 and (man_birth_day>=1 and man_birth_day<=21)):
    man_zodic="Sagittarius"
    
elif (man_birth_month==12 and (man_birth_day>=22 and man_birth_day<=31)) or (man_birth_month==1 and (man_birth_day>=1 and man_birth_day<=19)):
    man_zodic="Capricorn"

elif (man_birth_month==1 and (man_birth_day>=20 and man_birth_day<=31)) or (man_birth_month==2 and (man_birth_day>=1 and man_birth_day<=18)):
    man_zodic="Aquarius"
    
elif (man_birth_month==2 and (man_birth_day>=19 and man_birth_day<=29)) or (man_birth_month==3 and (man_birth_day>=1 and man_birth_day<=20)):
    man_zodic="Pisces"
       
else:
    man_zodic="Invalide date"
    
#woman

if (woman_birth_month==3 and (woman_birth_day>=21 and woman_birth_day<=31)) or (woman_birth_month==4 and (woman_birth_day>=1 and woman_birth_day<=19)):
    woman_zodic="Aries"
    
elif (woman_birth_month==4 and (woman_birth_day>=20 and woman_birth_day<=30)) or (woman_birth_month==5 and (woman_birth_day>=1 and woman_birth_day<=20)):
    woman_zodic="Taurus"
    
elif (woman_birth_month==5 and (woman_birth_day>=21 and woman_birth_day<=31)) or (woman_birth_month==6 and (woman_birth_day>=1 and woman_birth_day<=21)):
    woman_zodic="Gemini"
    
elif (woman_birth_month==6 and (woman_birth_day>=22 and woman_birth_day<=30)) or (woman_birth_month==7 and (woman_birth_day>=1 and woman_birth_day<=22)):
    woman_zodic="Cancer"

elif (woman_birth_month==7 and (woman_birth_day>=23 and woman_birth_day<=31)) or (woman_birth_month==8 and (woman_birth_day>=1 and woman_birth_day<=22)):
    woman_zodic="Leo"

elif (woman_birth_month==8 and (woman_birth_day>=23 and woman_birth_day<=31)) or (woman_birth_month==9 and (woman_birth_day>=1 and woman_birth_day<=22)):
    woman_zodic="Virgo"

elif (woman_birth_month==9 and (woman_birth_day>=23 and woman_birth_day<=30)) or (woman_birth_month==10 and (woman_birth_day>=1 and woman_birth_day<=22)):
    woman_zodic="Libra"

elif (woman_birth_month==10 and (woman_birth_day>=23 and woman_birth_day<=31)) or (woman_birth_month==11 and (woman_birth_day>=1 and woman_birth_day<=21)):
    woman_zodic="Scorpio"

elif (woman_birth_month==11 and (woman_birth_day>=22 and woman_birth_day<=30)) or (woman_birth_month==12 and (woman_birth_day>=1 and woman_birth_day<=21)):
    woman_zodic="Sagittarius"
    
elif (woman_birth_month==12 and (woman_birth_day>=22 and woman_birth_day<=31)) or (woman_birth_month==1 and (woman_birth_day>=1 and woman_birth_day<=19)):
    woman_zodic="Capricorn"

elif (woman_birth_month==1 and (woman_birth_day>=20 and woman_birth_day<=31)) or (woman_birth_month==2 and (woman_birth_day>=1 and woman_birth_day<=18)):
    woman_zodic="Aquarius"
    
elif (woman_birth_month==2 and (woman_birth_day>=19 and woman_birth_day<=29)) or (woman_birth_month==3 and (woman_birth_day>=1 and woman_birth_day<=20)):
    woman_zodic="Pisces"
       
else:
    woman_zodic="Invalide date"


if man_zodic=="Invalide date" or woman_zodic=="Invalide date":
    if man_zodic=="Invalide date" and woman_zodic!="Invalide date":
        print("Man can enter ",man_zodic)
        print("Woman Zudic is ",woman_zodic)
    else:
        print("Man Zudic is",man_zodic)
        print("Woman can enter ",woman_zodic)
else:
    print("Man Zudic is",man_zodic)
    print("Woman Zudic is ",woman_zodic)
    if man_zodic==woman_zodic:
        print("Love matched")
    elif (man_zodic in fire and woman_zodic in air) or (man_zodic in air and woman_zodic in fire):
        print("Love matched")
    elif (man_zodic in earth and woman_zodic in water) or (man_zodic in water and woman_zodic in earth):
        print("Love matched")
    elif (man_zodic in fire and woman_zodic in earth) or (man_zodic in earth and woman_zodic in fire):
        print("Complimentry matched")
    elif (man_zodic in water and woman_zodic in air) or (man_zodic in air and woman_zodic in water):
        print("Complimentry matched")
    else:
        print("Difficult to matched")