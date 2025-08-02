#WAP to print a factorial number accepted from the user
num=int(input("Enter any number:"))
f=1
i=1
while (i<=num):
    f=f*i
    i+=1
print("Factorial of a number is:",f)