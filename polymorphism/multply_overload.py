class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __mul__(self, other):
        a=self.a*other.a
        b=self.b*other.b
        a3=mul(a,b)
        return a3

a1=mul(45,67)
a2=mul(55,23)
a3=a1*a2
print(a3.b)

