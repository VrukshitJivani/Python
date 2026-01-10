rupees=int(input("Enter Rupees:"))

c_500=rupees//500
r500=c_500*500
print(f"{500}x{c_500}={r500}")

c_200=(rupees-r500)//200
r200=c_200*200
print(f"{200}x{c_200}={r200}")

c_100=(rupees-(r500+r200))//100
r100=c_100*100
print(f"{100}x{c_100}={r100}")

c_50=(rupees-(r500+r200+r100))//50
r50=c_50*50
print(f"{50}x{c_50}={r50}")

c_10=(rupees-(r500+r200+r100+r50))//10
r10=c_10*10
print(f"{10}x{c_10}={r10}")

c_2=(rupees-(r500+r200+r100+r50+r10))//2
r2=c_2*2
print(f"{2}x{c_2}={r2}")

c_1=(rupees-(r500+r200+r100+r50+r10+r2))//1
r1=c_1*1
print(f"{1}x{c_1}={r1}")
