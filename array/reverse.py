from array import *
arr=array('i',[])
for i in range(5):
    a=int(input("Enter values: "))
    arr.append(a)
print("Given array is: ")
for i in range(5):
    print(arr[i],end=" ")
print("\nReverse of the array is: ")
arr.reverse()
for i in range(5):
    print(arr[i],end=" ")



