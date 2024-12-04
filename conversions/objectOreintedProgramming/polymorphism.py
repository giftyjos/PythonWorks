# polymorphism(more than one form or more than many form)
# method_overloading(same method name and different number of parameters)

# method_overriding(parent clsil alreay method define chythtund then )



# method_overriding()

class Operations:

    def add(self,num1,num2):

        print(num1,num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)


obj=Operations()
obj.add(10,20,30)


# class Operations:

#     def add(self,*args): overloading  means *args 
#         print(sum(args))


# python core + advanced
