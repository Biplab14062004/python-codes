#WAP to sum the series   1+1/2+1/3+....+1/n
num1=int(input("Enter the range: "))
sum=0
for i in range(1,num1+1):
    sum+=1/i
print("The sum of the series is: ",sum)
