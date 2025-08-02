#WAP to display the student mark sheet
sub1=int(input("Enter the number in Bengali:"))
sub2=int(input("Enter the number in English:"))
sub3=int(input("Enter the number in Math:"))
sub4=int(input("Enter the number in Science:"))
sum=(sub1+sub2+sub3+sub4)
print(sum)
aggregate_number=((sum/400)*100)
print(aggregate_number)
if(aggregate_number>75):
    print("Grade is Distinction")
elif(aggregate_number>=60 and aggregate_number<75):
    print("Grade is 1st Division.")
elif(aggregate_number>=50 and aggregate_number<60):
    print("Grade is 2nd Division.")
elif(aggregate_number>=40 and aggregate_number<50):
    print("Grade is 3rd Division.")
else:
    print("Grade is Fail.")