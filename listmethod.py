A=[12,46,98,"Rakesh",'Babu','Sourav',20.98,True,False]
print(A[::-1])
A[3]='biplab'
print(A)
A[1:4]='sanaka',44,27
print(A)
B=[98,47,64,86]
A.extend(B)
print(A)
A.remove("Sourav")
print(A)
A.pop(6)
print(A)
del A[4]
print(A)
A.clear()
print(A)
del A
print(A)