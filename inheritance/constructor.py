class A:
    def __init__(self):
        print("a")
class B(A):
    def __init__(self):
        print("b")
        super().__init__()
ob=B()