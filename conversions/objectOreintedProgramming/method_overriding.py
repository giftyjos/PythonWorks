# methodoverriding(2classes then inherited and signature same)


class Parent:
    def mobile(self):
        print("samsunga35")

    def vehicle(self):
        print("passion pro")

class Child(Parent):
    def mobile(self):
        print("iphone")
    def vehicle(Self):
        print("tvs roinin")

child_instacnce=Child()
child_instacnce.mobile()
