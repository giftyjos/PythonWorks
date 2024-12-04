years_path="C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\years.txt"


century_year_path="C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\century year.txt"


leap_year_path="C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\leapyear.txt"

f_read=open(years_path,"r")

f_century=open(century_year_path,"w")

f_leapyear=open(leap_year_path,"w") #these are the reference 

def is_century_year(year):

    return True if year%100 == 0 else False

def is_leap_year(year):
     
     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True

     else:

        return False

for year in f_read:

    year=int(year)

    if is_century_year(year):

       f_century.write(str(year)+"\n")

    if is_leap_year(year):

       f_leapyear.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leapyear.close()
