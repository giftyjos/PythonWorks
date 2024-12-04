f=open("C:\\Users\\HP\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\fruits.txt","r")
fruits=[]#list
for line in f:
    
    fruits.append(line.rstrip("\n")) #rstrip=\n remove akkan riightsiden
print(fruits)#list aayi print aavum ith

# for line in f:
#     print(line) ith normal aayi print aavum


# this is two types