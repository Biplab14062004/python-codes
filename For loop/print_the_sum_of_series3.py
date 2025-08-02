#WAP to sum the series-     1/2 + 2/3 +...+ n/(n + 1) using for loop
num=int(input("Enter the range: "))
sum=0
for i in range(1,num+1):
    sum+=i/(i+1)
print("The sum of the series is:",sum)
