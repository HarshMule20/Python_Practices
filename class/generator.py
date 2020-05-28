'''def top():
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11
val=top()
print(val.__next__())
print(val.__next__())
print(val.__next__())
for i in val:
    print(i)'''

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
val=topten()
for i in val:
    print(i)




