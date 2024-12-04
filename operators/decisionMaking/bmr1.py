weight=int(input("enter weight:"))

height=int(input("enter height:"))

age=int(input("enter age:"))

gender=input("enter gender:").lower()
print(height, weight, age, gender)

if gender== "male":
    BMR=10*weight + 6.25 - 5 *age + 5
elif gender== "female":
    BMR=10*weight+6.25* height - 5*age -161
else:
    print("555555")
print(BMR)