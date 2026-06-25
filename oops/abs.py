from abc import ABC , abstractmethod

class paymentgateway(ABC) :
    @abstractmethod
    def pay(self):
        pass

class cardpay(paymentgateway):
    def pay(self):
        print("Paying bill using card")    

class UPIpay(paymentgateway):        
    def pay(self):
        print("Paying bill using UPI")           

class payment_gateway:
    def __init__(self , gateway):
        self.gateway = gateway

    def checkout(self ):
        print("Checking ...")
        self.gateway.pay()


p1 = payment_gateway(cardpay())        
p2 = payment_gateway(UPIpay())       


p1.checkout()
p2.checkout()
