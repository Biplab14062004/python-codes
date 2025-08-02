n=int(input("Enter the number of rows which you want: "))
for i in range(n):
    print(' ' * (n-i-1),end='')
    for j in range(i+1):
        if j%2==0:
            print("$",end=' ')
        else:
            print('*',end=' ')
    print()