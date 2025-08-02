#WAP to print mean in a list
numbers=[10,20,30,40,50]
total=0
for i in numbers:
    total+=i
mean=total/len(numbers)
print("The mean of the list is:",mean)