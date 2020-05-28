class val:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
v1=val(4,5)
v2=val(6,4)
print(v1)
print(v2)