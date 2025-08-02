#WAP to print half pyramid using odd number
row=int(input("Enter the number of rows which you want:"))
num=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(num,end=" ")
    num+=2
    print()