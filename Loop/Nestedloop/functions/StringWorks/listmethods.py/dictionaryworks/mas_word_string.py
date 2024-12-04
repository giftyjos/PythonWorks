

text="this is a simple programming question to find word with maximum number of characters"

# step1 split text to words

words=text.split(" ")

# words=['this','is','a','simple','programming','question','to','find','word','with','with','maximum',]

def get_count(w):
   
   return words.count(w)
most_frequent_word=max(words,key=get_count)
print(most_frequent_word)
# print(max(words,key=get_length))



# sort

# words=["hello","hai","morning","test","apple"]
# srt_words=sorted(words,key=get_length,reverse=True)
# print(srt_words)



# most recursive