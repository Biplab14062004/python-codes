#WAP to print double hill pattern 
row=int(input("Enter the number of the row which you want: "))
for i in range(1,row+1):
    print(" "*(row-i)+"* "*i,end="")
    print(" "*(2*(row-i)),end="")
    print(" *"*i)