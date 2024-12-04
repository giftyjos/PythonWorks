from re import finditer

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\processingJson\\regularexpressionWorks\\regularexp_file_works\\social_posts.txt")

for line in f:

     words=line.rstrip("\n")#check  out my new blog post! #blog #webdevelopment

     pattern="#\w+"

     matcher=finditer(pattern,words)

     for obj in matcher:

        print(obj.group())

