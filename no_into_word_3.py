nom=input('Enter a number under 100: ')
no=int(nom)
print('number is ',no)
last=no%10
first=no//10-2
list1=['Zero','one','two','three','four','five','six','seven','eight','nine']
list2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
list3=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
if no<10:
    print(list1[no])
elif no<=20 and no>9:
    print(list2[last])
elif no>20 and no<100:
    print(list3[first],end=' ')
    if last!=0:
        print(list1[last])
else:
 print('Number is not under 20 please enter a valide number')

 print(no2word(no))
