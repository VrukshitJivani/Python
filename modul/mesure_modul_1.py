import conveter as c

meter=float(input("Enter meter:"))
foot=float(input("Enter foot:"))
cm=float(input("Enter cm:"))

m_i=c.meterToInch(meter)
f_i=c.footToInch(foot)
c_i=c.cmToInch(cm)

print(f"Meter to inch is {m_i}")
print(f"Foot to inch is {f_i}")
print(f"Cm to inch is {c_i}")
