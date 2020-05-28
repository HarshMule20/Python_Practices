from array import *
arr=array('i',[])
for i in range(5):
    a=int(input("Enter values: "))
    arr.append(a)
print("Given array is: ")
for i in range(5):
    print(arr[i],end=" ")
print()
for i in range(4,-1,-1):
    print(arr[i],end=" ")



