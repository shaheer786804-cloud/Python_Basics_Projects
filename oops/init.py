class Device:

    Brand = "Omen"
    def __init__(self , name):
        print("Init is called" , name)
        self.name = name.upper()

    def show(self):
        print("Device : ", self.name)
    @classmethod
    def info(cls) :
        return cls.Brand
d1 = Device("Mobile")
d2 = Device("Laptop")

d1.show()
d2.show()
print(Device.info())

