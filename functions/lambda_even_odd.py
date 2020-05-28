from functools import *
nums=[2,6,3,4,9,8,5,70,43,76,23,87,56,96]
even=list(filter(lambda i:i%2==0,nums))         #use of filter function
double=list(map(lambda n:n*2,even))
sum=reduce(lambda a,b:a+b,double)

print(even)
print(double)
print(sum)