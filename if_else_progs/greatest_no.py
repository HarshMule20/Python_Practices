num1=int(input('Enter first number= '))
num2=int(input('Enter second number= '))
num3=int(input('Enter third number= '))
if num1>num2:
    if num1>num3:
        print('first number is greatest')
    else:
        print('third number is greatest')
else:
    if num2>num3:
        print('Second number is greatest')
    else:
        print('third number is greatest')
