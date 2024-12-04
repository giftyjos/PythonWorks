class GrandParent:
    def m(self):
        print("Grand parent class m method")


class Parent():

    def m(self):
        print("parent class m method")

# Error name ambiguity error[java]=>interface

class Child(GrandParent,Parent):

    def m3(self):

        print("child class m3 method")

child_instacnce=Child()

child_instacnce.m3()

child_instacnce.m()