#WAP to check if the given string is palindrome or not
# string=input("Enter a string: ")
# for i in string:
#     rev=string[::-1]
# if string==rev:
#     print("String is palindrome.")
# else:
#     print("String is not palindrome.")
given_string="madam"
reverse_string=" "  
for char in given_string:
    reverse_string=char+reverse_string  
if given_string==reverse_string:
    print("The string",given_string,"is a Palindrome.")
else:
    print("The string",given_string,"is NOT a Palindrome.")