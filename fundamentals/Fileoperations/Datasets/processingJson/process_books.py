
from  json import load

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\books.json")
data=load(f)
# for books in data:
#     print (books)

all_titles=[book.get("title") for book in data]

# print(all_titles)

# books with pages<250

page_filter=[book.get("title") for book in data if book.get("pages")<250]

print(page_filter)

# print all genres

all_genres=[book.get("genre") for book in data]

# print(all_genres)
genres_count={genre:all_genres.count(genre) for genre in all_genres}

print(genres_count)

# print costly book
costly_book=max(data,key=lambda d:d.get("price"))

print(costly_book)

#author with more than one book
all_author=[book.get("author") for book in data] 
# print (all_authors)

author_count={auth:all_author.count(auth) for auth in all_author}

print([k for k,v in author_count.items() if v >1])