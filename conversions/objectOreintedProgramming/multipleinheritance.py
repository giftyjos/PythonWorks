class Person:
    
    name:str

    age:int

    def__init__(self,name,age)

    self.name=name

    self.age=age
    
    def display_person_info(self):
     
       print(self.name,self.age)


class Employee:

    eid:int

    salary:int
    
    def__init__(self,eid,salary)

    self.eid=eid

    self.salary=salary

    def display_employee_info(self):
 
        print(self.eid,self.salary)



    class Manger(Person,Employee):

        department:str


        def__init__(self,age,name,eid,salary,department)

        Person.__init__(self,age,name)

        Employee.__init(self,eid,salary)

        self.department=department

    def display_manger_info(self):

        self.display_person_info()

        self.display_employee_info()

        print(self.department)


mange_instance=Manger(32,"hari","eo1",54000,"hr")

mange_instance.display_manger_info()



# Cusine(cusine_name)

# MealType(name)

# Dish(dish_name)

# indian,break_fast,gheeroast
# italian,
# break_fast
# pasta



# inhertance
# polymorphism
  # methodoverloding
  # methodoveriding