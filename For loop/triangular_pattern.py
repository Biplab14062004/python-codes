#wap to print a triangular pattern using for loop
row=int(input("enter the number of rows you want:"))
for i in range(0,row):
    for j in range(0,row-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()