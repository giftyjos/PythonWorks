class GrandParent:
    def m1(self):
        print("Grand parent class m1 method")

class Parent():
    def m2(self_):
        print("parent class m2 method")

class Child(Parent,GrandParent):
    def m3(self):
        print("child class m3 method")
    
child_instacnce=Child()

child_instacnce.m3()

child_instacnce.m2()

child_instacnce.m1()

# method oerriding  parent cls il m1 