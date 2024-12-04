f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\names.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:

    f.write(l+"\n")

f.close()

# for line in f:
#     print(line) this is  working string are only write