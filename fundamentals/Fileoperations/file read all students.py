
f1=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\all_students.txt")

f2=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\failed_stduents.txt")


all_students_set=set()

failed_students_set=set()
    
for line in f1:

    line=line.rstrip("\n")

    all_students_set.add(line)

for line in f2:


    line=line.rstrip("\n")

    failed_students_set.add(line)

passed_students=all_students_set.difference(failed_students_set)#intersection=difference

print(passed_students)

    