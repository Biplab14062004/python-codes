#WAP to print a list untill a negative number is encountered
list=[23,474,4747,43,45,-23,44,455,4553,564]
for i in list:
    if i<0:
        break
    print(i,end=" ")