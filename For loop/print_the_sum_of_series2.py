#WAP to sum the series   1/1² + 1/2²+ ... 1/n² using for loop
num=int(input("Enter the range: "))
sum=0
for i in range(1,num+1):
    sum+=1/(i**2)
print("The sum of the series is:",sum)
