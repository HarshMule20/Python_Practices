class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        a=self.a+other.a
        b=self.b+other.b
        a3=add(a,b)
        return a3

a1=add(45,67)
a2=add(55,23)
a3=a1+a2
print(a3.b)

