#WAP to inverted half pyramid using number
row=int(input("enter the number of rows you want:"))
num = row
for i in range(row,0,-1):
    for j in range(1,i+1):
       print(i, end=" ")
    num-=1
    print()