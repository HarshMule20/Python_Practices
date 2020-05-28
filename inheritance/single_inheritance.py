class A:
    def check(self):
        print("This is class A")
class B(A):
    def check(self):
        print("This is class B")
        super().check()
b1= B()
b1.check()