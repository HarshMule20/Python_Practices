from array import *
arr1=array('i',[2,3,4,5])
arr2=array('i',[])
for i in range(len(arr1)):
    a=arr1[i]
    arr2.append(a)
arr1[2]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))