#WAP find the average number in a list using for loop
numbers=[10,20,30,40,50]
total=0
for num in numbers:
    total+=num
average = total/len(numbers)
print("The average is: ",average)
