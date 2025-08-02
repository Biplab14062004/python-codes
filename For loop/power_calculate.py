#WAP to calculate power of a number
num=int(input("Enter a number:"))
pow=int(input("Enter the power:"))
for i in range(1,num):
    pow=num**pow
print("Result is:",pow)