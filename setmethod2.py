s1={'Biplab','Saikat','Devabrata','Rajibul','Debesh','Riya'}
s2={'Biplab','Saikat','Devabrata','Rajibul','kanchan'}
s3=s1.union(s2)
print(s3)
s4=s1|s2
print(s4)
s5={'kaka','jetha','vai','dada'}
s6=s1.union(s2,s5)
print(s6)
tuple1=('biplab','Krishna','Antima','Riya')
x=s6.union(tuple1)
print(x)
y=s1.intersection(s2)
print(y)
z=s1&s2
print(z)
# s1.intersection_update(s2)
# print(s1)
set1=s1.difference(s2)
print(set1)
set2=s2-s1
print(set2)
# s1.difference_update(s2)
# print(s1)
set3=s2.symmetric_difference(s1)
print(set3)
set4=s1^s2
print(set4)