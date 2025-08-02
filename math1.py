import cmath
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
w=(b**2)-(4*a*c)
R1=(-b+cmath.sqrt(w))/(2*a)
R2=(-b-cmath.sqrt(w))/(2*a)
print(R1,R2)