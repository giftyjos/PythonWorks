def review(rating):

    #too low < 0
    # too high > 10 

    if rating<0:
        raise Exception("too low")
    else:
        print("done!")
    
try:
        review (12)#error
except Exception as e:
        print(e)
print("hello")
print("hai")



# .....new.....



def poll(age):

        assert age>18,"invalid age"

        print("voted")
try:

   poll(14)

except Exception as e:

        print(e)

# ......new......

def review(rating):

        assert rating>0,"too low"

        assert rating in range(0,11),"too high"

print("rated")
