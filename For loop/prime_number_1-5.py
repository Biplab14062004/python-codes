#WAP to print all the prime number between 1 to 50 
for i in range (1,51):  
    if i > 1:  
        for num in range (2,i):  
            if ( i % num) == 0: 
                break  
        else:  
         print (i)