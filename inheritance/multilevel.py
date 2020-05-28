class A:
    def check(self):
        print("This is class A")
class B(A):
    def check2(self):
        print("This is class B")
class C(B):
    def check3(self):
        print("This is class C")

c1= C()
c1.check()
c1.check2()
c1.check3()