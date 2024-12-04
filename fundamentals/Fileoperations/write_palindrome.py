read_path="C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\words.txt"

write_path="C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\palindrome.txt"

f_read=open(read_path)

f_write=open(write_path,"w")

for line in f_read:

    word=line.rstrip("\n")#hello

    reversed_word=word[::-1]#reversed_word=olleh

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()
    
f_write.close()
   
