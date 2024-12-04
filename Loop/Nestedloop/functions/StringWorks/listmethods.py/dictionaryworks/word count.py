text="this is a simple program this program count the count this program is simple"
# word count
# {this:3,is:2}

# step1 split text as words

words=text.split(" ")

print(words)#['this','is','as','simple','prgrm','this','program','count','the']

# ....nxt qn...

words=["hai","hello","hai","hello"]

word_count={}

# iterate words

for w in  words:
    # chck w exist in words
    if w in word_count:
        word_count[w]+=1
    else:
        # add w as  key in  word_count and value as 1

        word_count[w]=1
    print(word_count)
