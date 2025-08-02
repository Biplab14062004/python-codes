#WAP to find the sum of following series   1+8+27+.....+n terms
digit=int(input("Enter any number:"))
i=1
sum=0
while i<=digit:
    sum+=i**3
    i+=1
print("The sum of the series is:",sum)