# student[id,name,course]
# set_student()
# display_student()

class Student:

    name:str

    rolnumber:int

    age:int

    course:str
#initialzing attributes of student class
def set_student(self,name,rolnumber,age,course):
                       #def()-method, self name,selfrolnumber(parameters),(attributes)-name,rolnumber,age

    self.name=name

    self.rolnumber=rolnumber

    self.age=age

    self.course=course

def display(self):

    print(self.name,self.age,self.rolnumber,self.course)

# reference_name=ClassName()

Student_instance1=Student()


Student_instance1.set_student("gifty",100,35,"django")

Student_instance1.display()




# intilazing instacne variables constructor
# java(classname)

# python-> __init__    (ithan pythonil consturctor use is instance variable ne(initilaze cheya))