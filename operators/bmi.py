#program for calculating bmi(bodymassindex)

 #BMI=weight_in_kg/(height_in_metre)**2

weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter  height in cm:6"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre**2

BMI=round(BMI,2) #utilityFunctions->#round(object,precision)

print(BMI)

#jst print(BMI) output=20.2222567
#then BMI=round(BMI,2)->less floating point means 20.22(changes ,2 or 3)