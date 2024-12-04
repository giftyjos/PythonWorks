
words=["hello","hai","hello","this","is","hello"]

# word_frequency

word_frequency={w:words.count(w) for w in words} #{'hello':3,'hai':1,'this':2,'is':2'}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)# recursive word means koodthal time vanna word hello this word is printed 

# ....display non_frequency_words....

words=["hello","hai","hello","this","is","hello"]

# word_frequency

word_frequency={w:words.count(w) for w in words} #{'hello':3,'hai':1,'this':2,'is':2'}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v<1]

print(recursive_words)

# display most_recursive ?
# 
# display non_most_recursive ?
# ==1


# get(key)
# pop(key)
# keys()
# values()
# items()


text="ABBACB"


# print character count
# A:2
# B:3
# C:1
char_count={}

for ch in text:
    if ch in char_count:
       char_count[ch]+=1
    else:
        char_count[ch]=1
print(char_count)

# first recursive character
# dictionary methods