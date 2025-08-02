#Wap to check a number is prime or not using while loop
num1=int(input("Enter any number:"))
a=0
if num1==0:
    print('Not a prime number.')
else:
    i=2
    while i<num1:
        if num1%i==0:
            a=a+1
        i+=1
if a==0:
    print(num1,"is a prime number.")
else:
    print(num1,"is not a prime number.")