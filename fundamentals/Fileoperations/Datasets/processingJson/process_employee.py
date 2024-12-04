
from  json import load

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\employee.json")

data=load(f)
for emp in data:
    print (emp)