# end
# read from user
# print all even numbers from begin to end

begin=int(input(" enter starting limlit"))#50
end=int(input("enter ending limit"))#10

# 10,,,,,,,50
# begin    end

if begin>end:

   begin,end=end,begin
i=begin#i=50

while(i<=end):#50<=10

    if 1%2!=0: #odd-(!=)  #even(==)

        print(i)

    i=i+1




    # read two limits
    # sample output(1)
        # start=2
        # end=10
    # sample output(1) 
        #even 
        # 2,4,6,8
    # sample input(2)
        # start=10
        # end=2
    # sample output(1)
        # even
        # 8,6,4,2


