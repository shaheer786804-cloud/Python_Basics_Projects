class A():
    def __init__(self):
        print("In INIT A")
    def f1(self) :
        print("F1 is at working")

class B(A):
    def __init__(self):
        print("In INIT B")
        super().__init__()
    def f2(self) :
        super().f1()
        print("F2 is at working")


obj2 = B()

obj2.f2()
