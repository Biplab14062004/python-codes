#WAP to print table of a number entered from the user
i=1
num=int(input("Enter a number:"))
print("Table is",num,"is:")
while(i<=10):
    print(num,"*",i,"=",i*num)
    i+=1
