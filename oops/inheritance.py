class A():
    def f1(self) :
        print("F1 is at working")
    def f2(self) :
        print("F2 is at working")
    def show(self):
        print("In class A")

class B(A):
    def f3(self) :
        print("F3 is at working")
    def f4(self) :
        print("F4 is at working")
    def show(self):
        print("In class B")

class C(B):
    def f5(self) :
        print("F5 is at working")
    def f6(self) :
        print("F6 is at working")



obj1 = C()
C.show(obj1)
