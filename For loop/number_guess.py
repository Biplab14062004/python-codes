#WAP to guess a number between 1-9
# num=int(input("Enter a number:"))
# while(num<10):
#     if num>0 and num<10:
#         print("Congratulations. You Are Right Guessed.")
#         break
# else:
#     print("Sorry! Enter a vaild number between 1-9.")
import random
target_number,guess_number=random.randint(1,10),0
guess_number=int(input("Guess a number between 1-10 until you get it right: "))
while(target_number!=guess_number):
    print("Well Guessed.")