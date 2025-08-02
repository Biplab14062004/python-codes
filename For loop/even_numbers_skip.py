#WAP to print 1 to 10 without even number
for i in range(1,11):
    if i%2==0:
        continue
    print(i,end=" ")