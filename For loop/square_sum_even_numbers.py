#WAP to sum of square of even numbers
num=int(input("Enter the range: "))
sum=0
print("The square of even numbers are: ")
for i in range(1,num):
    if(i%2==0):
        square=i**2
        sum+=square
        print(i**2)
print("The sum of all even numbers squares: ",sum)