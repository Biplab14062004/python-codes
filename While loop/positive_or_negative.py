#WAP to enter the numbers till the user enter zero and at the end display the count of positive and negative number
positive_num=0
negative_num=0
print("Enter a number for continue and 0 for exist.")
while True:
   num=int(input("Enter the numbers:"))
   if num==0:
      break
   elif num>0:
    positive_num+=1
   elif num<0:
    negative_num+=1
print("The count of positive numbers is:",positive_num)
print("The count of nagative numbers is:",negative_num)