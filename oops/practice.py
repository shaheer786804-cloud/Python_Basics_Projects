class students:
    def __init__(self , name , grade , age):
        self.name = name
        self.grade = grade
        self.age = age

    def information(self):
        print("Information of a Student : " , self.name , self.grade , self.age)


student_1 = students("Ali" , "A" , "15")
student_2 = students("Ahmed" , "A+" , "16")
student_3 = students("Ayyan" , "b" , "16")


student_1.information()
student_2.information()
student_3.information()