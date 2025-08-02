#WAP to display all leap years from 1900 to 2024
print("Leap Years are:")
for i in range(1900,2024):
    if(i%4==0):
        print(i,end=" ")