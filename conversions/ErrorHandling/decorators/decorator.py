class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_age(self):
        return self.age

    @property
    def get_name(self):
        return self.name

# Create an instance of Person
person_instance = Person("hari", 34)

# Use the instance
print(person_instance.get_name)
print(person_instance.get_age)
