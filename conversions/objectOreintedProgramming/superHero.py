class SuperHero:
    name: str
    suit: str

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def __str__(self):
        return self.name

class SpiderMan(SuperHero):
    def __init__(self, name, suit):
        super().__init__(name, suit)

    def super_power(self):
        print("spider sense", "web shooting", "sticky hands")

# Create an instance of SpiderMan
spiderman = SpiderMan("Peter Parker", "Red and Blue")

# Use the instance
print(spiderman)
spiderman.super_power()
