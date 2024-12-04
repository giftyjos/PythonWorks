

text="ABABBCCDDE"
# string
# character_frequency{A:2,B:3}

character_frequency={ch:text.count(ch)for ch in text}

print(character_frequency)

# for k,v in character_frequency.items():

#     if v==1:

#        print(k)

non_recursive_character=[k for k,v in character_frequency.items() if v==1]

print(non_recursive_character)
