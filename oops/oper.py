class account:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return( f"{self.name} : {self.balance}")
    
    def __add__(self, other):
        return self.balance + other.balance
    

Person1 = account("Ali" , 1500)
Person2 = account("Hashir" , 3000)
combined = Person1 + Person2
print(Person1)
print(Person2)
print(combined)

if Person1.balance > Person2.balance :
    print(f"{Person1.name} will pay bill")
else:
    print(f"{Person2.name} will pay bill")
