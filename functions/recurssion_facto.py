def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

num=int(input("Enter the number: "))
print("Factorial is: ",fact(num))