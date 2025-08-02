#write a program to check vowel or not
char=(input("Enter a character:"))
vowel=["a","e","i","o","u"]
if(char in vowel):
    print("The character is vowel.")
else:
    print("The character is consonant.")