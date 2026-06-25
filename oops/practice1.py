# Practice of init function
class students:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def show (self):
        print("Students information:" , "Name :" ,self.name , "Age :" , self.age)

stu1 = students("M Shaheer" , 15)        
stu2 = students("Ahmed Husnain" , 16)    

stu1.show()
stu2.show()
