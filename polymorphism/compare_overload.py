class compare:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __gt__(self, other):
        a=self.a+self.b
        b=other.a+other.b
        if a>b:
            return True
        else:
            return False
a1=compare(8,9)
a2=compare(6,5)
if a1>a2:
    print("A1 is greater")
else:
    print("A2 is greater")
