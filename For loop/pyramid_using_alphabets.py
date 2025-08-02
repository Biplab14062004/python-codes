#WAP to print half pyramid using alphabets using for loop
row=int(input("Enter the number of rows which you want:"))
num=65
for i in range(0,row):
    for j in range(0,i+1):
       ch=chr(num)
       print(ch,end=" ")
    num=num+1
    print()