class car:
    wheels=6                #static/class variable
    def __init__(self):
        self.mil=10         #instance variable
        self.com="BMW"
c1=car()
c2=car()
car.wheels=19
c1.wheels=12
c1.mil=4
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)