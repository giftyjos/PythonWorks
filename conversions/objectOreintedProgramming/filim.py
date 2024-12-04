# movie

# title,rating,run_time.director,genreclass Student:
class Movie:

    id:int

    title:str

    run_time:int

    director=str

    genre:str
#initialzing attributes of movie class
    def set_movie(self,id,title,rating,director,run_time,genre):
                       #def()-method, self name,selfrolnumber(parameters),(attributes)-name,rolnumber,age

       

     def display(self):

        print(self.id,self.title,self.genre)

filim_instance1=Movie()

# reference_name=ClassName()

filim_instance1.set_movie(100,"arm",4.5,"jithin lal",120,"action")

filim_instance1.display()