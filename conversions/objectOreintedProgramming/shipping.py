class Shipping:

    def calculate_shipping_cost(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self,weight):
        print(weight*20)

    class StandardShipping(Shipping):

        def calculate_shipping_cost(self,weight):
            print(weight*10)


expe_instance=ExpressShipping()
expe_instance.calculate_shipping_cost(10)
Std_instance=StandardShipping()
Std_instance.calculate_shipping_cost(10)

# ExpressShipping=> weight*2
# StandardShipping =>weight*10


# polymorpism
    # method_overloading()
    
# class
# object
# __init__
# super()
# self
# inheritance
   #single
   #multilevel
   #multiple
# polymorphism
    #methodoveroading
    #methodoverrind
# Abstraction
      #hiding implementation details
