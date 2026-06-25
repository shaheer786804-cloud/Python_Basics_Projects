class dog:
    def sound(self):
        print("Dog Barks")

class cat:
    def sound(self):
        print(" Cat meows")

class trainer:
    def train(self , animals):
        print("Training Starts...")
        animals.sound()

D = dog()
C = cat()

t = trainer()

t.train(C)