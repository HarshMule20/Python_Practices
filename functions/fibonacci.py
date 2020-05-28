def fibonacci(last):
    a=0
    b=1
    if last==1:
        print(a)
    elif last<=0:
            print("Invalid number")
    else:
        print(a)
        print(b)
        for i in range(2,last):
            c = a+b
            a = b
            b = c
            print(c)


last=int(input("Enter the no. of fibonacci series: "))
fibonacci(last)