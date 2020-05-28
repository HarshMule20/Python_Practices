from array import *
arr=array('i',[])
for i in range(5):
    a=int(input("Enter value= "))
    arr.append(a)
print(arr)
for i in range(5):
    if(i==2):
        arr.remove(arr[i])
        break
print(arr)