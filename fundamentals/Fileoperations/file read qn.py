f=open("C:\\Users\\HP\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\qn.txt","r")

words=[]

for line in f:

    # line=this is a python program to print hello_word

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

    word_count={w:words.count(w) for w in words}#words count print

nested_word_count=[{v,k} for k,v in word_count.items()]

# word-key count-value reverse word-value,count-key

print(sorted(nested_word_count,reverse=True))




# sample={"apple:200,"mango":80,"banana":20} this is dictionary

# descending orderil sort cheyanam value vach 
# apple:200
# ṃango:80