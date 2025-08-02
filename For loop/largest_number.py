#WAP find the largest number in a list using for loop
numbers=[10,24,45,6,88,3]
largest=numbers[0]
for number in numbers:
    if number>largest:
        largest=number
print("The largest number is: ",largest)