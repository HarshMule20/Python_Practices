def add(a,b):
    return a+b
def add2(func):
    def modify(a,b):
        if a<0:
            print(" a is a negative number")
        return func(a,b)
    return modify
add=add2(add)
x=add(-2,8)
print(x)
