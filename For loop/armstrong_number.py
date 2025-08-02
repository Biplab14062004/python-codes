#WAP to check if a given number is an armstrong number or not using for loop
num=int(input("Enter a number: "))
sum=0
len=len(str(num))
for digit in str(num):
    sum+=int(digit)**len
if sum==num:
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")
