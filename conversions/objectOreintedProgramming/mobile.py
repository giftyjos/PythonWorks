class Mobile:

    name:str

    price:int

    brand:str

    def __init__(self,name,price,brand):   #__init__means construtor for python  self intance of init
    

       self.name=name

       self.price=price

       self.brand=brand

def display(self):

    print(self.name,self.price,self.brand)
    
mobile_instance1=Mobile("samsung",28000,"samsunga34")

mobile_instance1.display()