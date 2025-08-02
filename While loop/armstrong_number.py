# WAP to check whether a number is armstrong number or not
num=int(input("Enter a valid Number: "))
sum=0
n=len(str(num))
temp=num
while(temp>0):
   digit=temp%10
   sum+=digit**n
   temp//=10
if(num==sum):
   print(num,"is an Armstrong Number")
else:
   print(num,"is not an Armstrong Number")