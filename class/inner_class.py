class A:
    def __init__(self):
        self.a=19
        self.ob3=self.B()       #calling inside
    def show(self):
        print("Value of the outer class")
        print(self.a)
        print("in another show method using the inner object")
        self.ob3.show()
    class B:
        def __init__(self):
            self.b=28
        def show(self):
            print(self.b)
ob1=A()
ob2=A.B()                   #directly calling outside
ob1.show()
print("using outer class name ")
ob2.show()
print("using the object of the outer class.inner class")
ob1.ob3.show()
ob4=ob1.ob3                     #creating another object of inner
print("Creating the object using the outer class object.inner class object")
                                # class using the object of outer class
ob4.show()