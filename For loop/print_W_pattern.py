rows = 5
for i in range(rows):
    print(" "*i,end="")
    print(" $",end="")
    print(" "*(rows-i-1),end=" ")
    print(" *",end="")
    print(" "*(2*i-1),end=" ")
    if i>0:
        print("*",end="")
    print(" "*(rows-i-1),end=" ")
    print("$")