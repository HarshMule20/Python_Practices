num=int(input("Enter a number: "))
for i in range(2,num//2):
    if num%i==0:
        temp=1
        break
    else:
        temp=0
if temp==0:
    print("prime number")
else:
    print("nOt a prime number")