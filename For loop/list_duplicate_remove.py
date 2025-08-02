#WAP to remove duplicate values from a list using for loop
main_list=[1,1,2,3,2,4,22,45,34,22,4,23,34]
list=[]
for i in main_list:
    if i not in list:
        list.append(i)
print("Main list is:",main_list)
print("After remove the duplicate values:",list)
list.sort()
print("after sorting values:",list)