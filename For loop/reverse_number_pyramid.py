#WAP TO PRINT REVERSE NUMBER FROM 10 TO 1
start=1
stop=2
current_num=stop
for i in range(2,6):
    for j in range(start,stop):
        current_num-=1
        print(current_num,end=" ")
    print(" ")
    start=stop
    stop+=i
    current_num=stop