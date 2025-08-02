#WAP a python program to display all numbers within a range except the prime numbers input by the user using for loop
for i in range(1,31):  
    if i>1:  
        for num in range(1,31):  
            if(i%num!=0) and (i%2!=0):  
                break  
        else:
            print(i)