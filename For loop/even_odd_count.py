#WAP to count the number of even or odd from a series of numbers
numbers=[3,43,7,6,4,64,24,2,33,11,18,20]
count_even=0
count_odd=0
for num in numbers:
    if(num%2==0):
        print(num,"is Even Number")
        count_even+=1
    else:
        print(num,"is Odd Number")
        count_odd+=1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)