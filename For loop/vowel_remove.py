#WAP remove the vowel from the string user define string uses
string=input("Enter a string:-")
result=""
vowels="AEIOUaeiou"
for char in string:
    if char not in vowels:
        result+=char
print("String is without Vowels:",result)