#WAP to check the validity of a password input by the user using for loop
password=input("Enter a Passkey: ")
valid_len=False
lower_case=False
upper_case=False
digits=False
special_char=False
if (len(password)>=8) and (len(password)<=16):
    valid_len=True
    for i in password:
        if (i.islower()):
            lower_case=True
        if (i.isupper()):
            upper_case=True
        if (i.isdigit()):
            digits=True
        if (i=="!" or i=='@' or i=='#' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*'):
            special_char=True
if (valid_len==True and lower_case==True and upper_case==True and digits==True and special_char==True):
    print("Valid Password.")
else:
    print("Not a Valid Password!!!")