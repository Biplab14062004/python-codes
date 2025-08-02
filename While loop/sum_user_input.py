#WAP to enter the numbers till user wants and display the sum of all numbers
sum=0
print("Enter the number for continue and 0 for exist.")
while True:
    num=int(input("Enter the number:"))
    if num==0:
        break
    sum+=num
print("The sum of numbers is:",sum)