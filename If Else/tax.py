#write a program to calculate the tax
tax_amount=(int(input("Enter your amount:")))
MIN1=150001
MAX1=300000
MIN2=300001
MAX2=500000
MIN3=500001
RATE1=0.10
RATE2=0.20
RATE3=0.30
if(tax_amount<=150000):
   print("no tax")
elif(tax_amount>=MIN1 and tax_amount<=MAX1):
    print("TAX=",tax_amount*RATE1)
elif( tax_amount>=MIN2 and tax_amount<=MAX2):
    print("TAX=",tax_amount*RATE2)
else:
    print("TAX=",tax_amount*RATE3)