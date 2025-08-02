#WAP to count the vowel in a string
string="Biplab Das Modak"
vowel=['a','e','i','o','u','A','E','I','O','U']
vowel_count=0
for i in string:
    if i in vowel:
        vowel_count+=1
print(vowel_count)