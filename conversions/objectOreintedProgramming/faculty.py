

class Faculty:

    id:int

    name:str

    age:int

    course:str

    experience:int

    salary:int

    def set_faculty(self,id,name,age,course,experience,salary):

        self.id=id

        self.name=name

        self.age=age

        self.course=course

        self.experience=experience

        self.salary=salary

    def display_faculty(self):

           print(self.name,self.age,self.course)

# reference_name=ClassName()

faculty_instance1=Faculty()
faculty_instance2=Faculty()


faculty_instance2.set_faculty(100,"gifty",30,"django",4,2000)

faculty_instance2.display_faculty()


