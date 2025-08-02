#WAP to display the number names of a digits of a number entered by the user
num=input("Enter any number:")
a=list(num)
l=len(a)
i=0
x={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
while (i<l):
    print(x[int(a[i])],end=' ')
    i+=1