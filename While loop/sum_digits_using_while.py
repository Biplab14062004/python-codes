#wap to find a sum of digits of a number accepted from the user using while loop
x=int(input("Enter a number:"))
r=0
sum=0
while x!=0:
    r=x%10
    sum+=r
    x=x//10
print("Sum is",sum)