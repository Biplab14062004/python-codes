#WAP get the smallest number from the list
list_1=[100,33,44,24,84,56]
smallest=list_1[0]
for i in list_1:
    if i<smallest:
        smallest=i
print("The smallest number is:",smallest)