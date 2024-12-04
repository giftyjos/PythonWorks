num=int(input("enter numbers"))

while(num!=0):#541!=0 54!=0 5!=0 5!0 0!=0
    digit=num%10 #541%10=1 54%10=4 5%0 0!=0
    print(digit)#1 4 5
    num=num//10#num=541//10=54 54//10=5 5//10=0

    #extract digits