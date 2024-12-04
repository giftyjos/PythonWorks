#BMI=weight_in_kg/(height_in_metre)**2

weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter  height in cm:"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/(height_in_metre)**2

BMI=round(BMI,1) #utilityFunctions->#round(object,precision)

print(BMI)

if BMI <19: #0-18 range

    print("underweight")

elif BMI>=19 and BMI<25:#19-24 range

    print("normal weight")

elif BMI>=25 and BMI<30:#25-29

    print("over weight")

elif BMI>=30:#30>

    print("obese")



#print under weight if bmi<19
#print normal weight if bmi 19 to <25 
# print overweight if bmi 25 to <30
# print obese if bmi >=30