import random as rd
import string as st

pass_char=st.punctuation+st.ascii_lowercase+st.ascii_uppercase+st.digits
list=list(pass_char)
print(list)
 
password=[]
l=len(list)-1
i=0
while i<=10:
    password.append(str(rd.choice(pass_char)))
    i+=1
password=''.join(password)
print(password)