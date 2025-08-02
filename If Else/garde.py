#write a program to display the grade card
num=(int(input("Enter your number:")))
if(num<25):
    print("Grade D")
elif(num>25 and num<45):
    print("Grade C")
elif(num>45 and num<50):
    print("Grade B")
elif(num>50 and num<60):
    print("Grade B+")
elif(num>60 and num<80):
    print("Grade A")
else:
    print("Grade A+")