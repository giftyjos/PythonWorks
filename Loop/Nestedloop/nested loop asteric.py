
#  C1      C2      C3
#1 *       *       *
#2 *       *       *
#3 *       *       *
#4 *       *       *
#5 *       *       *                                         
#6 *       *       *                                            



for row in range(1,7):

    for col in range(1,4):

        print("*",end="\t")

    print()


    # $ $
    # $ $ $ 
    # $ $ $ $
    # $ $ $ $ $


for row in range(1,7): #row=2
    for col in range(1,row+1): # col in range(1,3+1)  #1 2
        print("$",end="\t")#$
    print()


# 1
# 2 3
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for row in range(1,6): #[1,2,3,4,,5]

    for co in range(1,row+1):# for col in(1,3)1 2
        print("row",end="\t") #col

    print()


    #5* * * * * col in range(1,6)
    #4 * * * * range(1,5)
    #3 * * * range(1,4)
    #2 * * range(1,3)
    #1 *range(1,2)

    for row in range(5,0,-1): #[1,2,3,4,,5]

      for col in range(1,row+1):# for col in(1,3)1 2

        print("*",end="\t") #col

    print("")


for row in range(1,6):#row(1)

    for col in range(5,row-1,-1):# range(5,0,-1) range(5,1,-1) range(5,2,-1)

        print("*",end="\t")
    print()


# hw full pyramid

