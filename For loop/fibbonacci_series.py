#WAP to get fibonacci series between 0-50 using for loop
first_num=1
second_num=1
print(first_num,end=" ")
print(second_num,end=" ")
for i in range(0,7):
    next_num=first_num+second_num
    print(next_num,end="  ")
    first_num=second_num
    second_num=next_num
    i+=1