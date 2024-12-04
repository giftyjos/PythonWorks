text="pneumonoultramicroscopicsilicovolcanoconiosis"
# print vowels
# print consonants


text="pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0
c_count=0

vowels_sequence=("a","e","i","o","u")

for ch in text:


    if ch in vowels_sequence:         #if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u")

        v_count=v_count+1
    else:
        c_count+=1

print("vowels count=",v_count)
print("cosonants count",c_count)



