#wap to find a product of the digits of a number
number=int(input("Enter a number:"))
r=0
product=1
while number!=0:
    r=number%10
    product*=r
    number=number//10
print("Product is",product)