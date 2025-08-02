#WAP to display divisible by 11 but not by 2 between 100 to 500
for i in range (100,501):
    if(i%11==0 and i%2!=0):
       print(i,end=" ")