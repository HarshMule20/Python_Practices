def update(lst):
    print(id(lst))
    lst[2]=40
    print(id(lst))
    print("lst 2: ",lst)
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst 1: ",lst)