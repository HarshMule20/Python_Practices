class addition:
    #def __init__(self):
    #    self.a = int(input("Enter the first value: "))
    #    self.b = int(input("Enter the second value: "))
    def show(self,a,b):
        self.a=a
        self.b=b
        self.c= self.a +self.b
        print("Addition: ",self.c)


obj=addition()
obj.show(7,8)