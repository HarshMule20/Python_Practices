class addition:
    #def __init__(self):
    #    self.a = int(input("Enter the first value: "))
    #    self.b = int(input("Enter the second value: "))
    def show(self,a,b):
        self.a=a
        self.b=b
        if self.a==self.b:
            return True


obj=addition()
if obj.show(7,7):
    print("They are same")
else:
    print("They are different")
