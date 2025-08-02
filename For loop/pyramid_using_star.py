#WAP to inverted half pyramid using star using for loop
row=int(input("Enter the numbers of rows you want:"))
for i in range(0,row+1):
    for j in range(0,row-i):
        print("*",end=" ")
    print()