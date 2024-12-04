movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]
# [count movies
print(len(movies))
# ]

#[ print all movie titles
for m in movies:#m={"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160}
    print(m.get("title"))
# list comperhension 
movies_title=[m.get("title") for m in movies]
print(movies_title)
# ]

#[ movies released in 2024
for m in movies:
    if m.get("year")==2024:
        print(m.get("title"))

# list comperhension
movies_year_filter=[m.get("title") for m in movies if m.get("year")==2024]
print(movies_year_filter)
# ]

# [ malayalam movie titles
malayalam_movies=[m.get("title") for m in movies if m.get("language")==2024]
print(malayalam_movies)
# ]

# [movie with highest runtime

def get_run_time(dictionary):
    return dictionary.get("run_time")
print(max(movies,key=get_run_time))
#   or

print(movies,key=lambda d:d.get("run_time"))

min(movies,key=lambda d:d.get("run_time"))
#  or
highest_runtime_movie=max(movies,key=lambda d:d .get("run_time"))
print(highest_runtime_movie.get("title"))
# ]

# malayalam movie counts

malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]
print(len(malayalam_movies))


# in which year most number of  movie released

all_years=[m.get("year") for m in movies]
# [2018,2023,2024,2024,2024,2024,2024]
# {2018:1,2023:1,2024:5}
year_count={y:all_years.count(y) for y in all_years}

print(year_count)