#WAP to find the common element in two list
list1=[10,20,30,40]
list2=[5,10,15,20]
common_element=[]
for i in list1:
    if i in list2:
        common_element.append(i)
print("COMMON ELEMENT:",common_element)