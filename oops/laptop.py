# define a laptop Class
#Inside it ,Create a meathod details
# inside it create two laptop objects
#Call the detail() method passing the different values

class laptop:
    def laptop1_properties(self):
        print("Name : Omen \n" \
        "RAM : 16GB")
    def laptop2_properties(self):
        print("\nName : Dell \n" \
        "RAM : 8 GB")

laptop1 = laptop()
laptop2 = laptop()
laptop1.cpu = "i7"
laptop1.laptop1_properties()
laptop2.laptop2_properties()
