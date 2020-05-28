def fact(no):
    facto=1
    for i in range(1,no+1):
        facto=facto*i
    return facto

num=int(input("Enter the no. to find the factorial: "))
print("Factorial is: ",fact(num))