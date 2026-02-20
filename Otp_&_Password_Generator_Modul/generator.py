#password generator 
def password_gen(size):
    import random as rd
    import string as st
    pass_char=st.punctuation+st.ascii_lowercase+st.ascii_uppercase+st.digits
    pass_list=list(pass_char)
    password=[]
    size=size-1
    i=0
    while i<=size:
        password.append(str(rd.choice(pass_list)))
        i+=1
    password=''.join(password)
    return password

#otp generator

def otp_gen(size):
    import random
    i=0
    list=[]
    while i<=size-1:
        list.append(str(random.randint(0,9)))
        i=i+1
    otp=''.join(list)
    return otp
