#Wap to print the fibonacci series till n terms using while loop
n=int(input("How many terms you want in fibonacci series:"))
if n==1:
    print('1')
elif n==2:
    print('1 1')
elif n<=0:
    print("please enter positive number greater than zero.")
else:
    first_t=1
    second_t=1
    print(first_t,end=' ')
    print(second_t,end=' ')
    i=2
    while (i<n):
        next_t=first_t+second_t
        print(next_t,end=" ")
        first_t=second_t
        second_t=next_t
        i+=1