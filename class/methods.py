class method:
    val=23
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def addition(self):
        print(self.m1+self.m2+self.m3)
    @classmethod
    def getval(cls):
        print("class method")
    @staticmethod
    def info():
        print("Static method")
s1=method(45,56,87)
s1.addition()
method.getval()
method.info()

