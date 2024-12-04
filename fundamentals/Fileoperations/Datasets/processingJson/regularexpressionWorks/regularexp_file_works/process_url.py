from re import findall

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\processingJson\\regularexpressionWorks\\regularexp_file_works\\urls.txt")
content=f.read()

pattern="https?://[\w\s./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)