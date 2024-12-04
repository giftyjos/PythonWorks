# 



# sample input(2)
  #start =20
  #end=2
#sample output(1)
    #  even
    # 8,6,4,2


# begin=int(input("enter start"))
# end=int(input("enter end"))
# reverse=False
# if begin>end:

#     reverse=True
#     i=begin
# while():
#     if 1%2==0:
#         print(i)
#     if reverse==True:
#         i=i+1
#     else:
#         i=i+1

begin=int(input("enter start"))

end=int(input("enter end"))

i=begin

reverse=False

if begin>end:
    reverse=True
    condition=i<=end

else:
    reverse=False
    condition=i>=begin

while(i<=end if reverse==False else i>=end):

    if i%2==0:

        print(i)

    if reverse==True:

        i=i-1

    else:

        reverse=False

        i=i+1






