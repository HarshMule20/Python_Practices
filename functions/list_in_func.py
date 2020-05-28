def count(lst):
    even=0
    odd=0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

lst=[24,23,62,74,97,33,67,12,98,45,61,39,84]
even, odd= count(lst)
print("No of even numbers: ",even)
print("No of odd numbers: ",odd)
