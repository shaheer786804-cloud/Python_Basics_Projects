class A():
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")
        super().show()

obj1 = B()
obj1.show()
