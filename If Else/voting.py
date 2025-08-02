age=int(input("Enter His Age:"))
if(age>=18):
    print("Eligible for voting.")
else:
    print("Not Eligible for voting.")
    difference=(18-age)
    print(difference,"years late to your vote")