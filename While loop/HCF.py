#WAP to find the HCF of two numbers entered from the user
number1=int(input("Enter First Number: "))
number2=int(input("Enter Second Number: "))
while number2 != 0:
    temp = number2
    number2 = number1 % number2
    number1 = temp
print("The HCF of two numbers is: ",number1)
