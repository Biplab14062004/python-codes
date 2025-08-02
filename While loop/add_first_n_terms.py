#WAP to add first n terms of the following series using while loop:     1/1!+1/2!+1/3!+....+1/n!
num1=int(input("Enter any number:"))
sum=0
f=1
i=1
while (i<num1):
    f=f*i
    sum=sum+i/f
    i+=1
print("number is",sum)