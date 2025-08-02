#WAP to classify a given number as prime or composite number
num=int(input("Enter a number:"))
compo=0
for i in range(2,num):
    if num%i==0:
        compo=1
        break
if compo==1:
    print("composite")
else:
    print('prime')