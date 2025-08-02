#WAP to print a specified list after removing the 0th, 4th and 5th element
original_list=[1,2,3,4,5,6,7]
original_list=[x for (i,x) in enumerate(original_list) if i not in (0,4,5)]
print("After removing values:",original_list)