#WAP to print half pyramid using number
row=int(input("enter the number of rows you want:"))
for i in range(0,row):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()