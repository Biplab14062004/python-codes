number=int(input("Enter the number of rows which you want: "))
for i in range(number,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()