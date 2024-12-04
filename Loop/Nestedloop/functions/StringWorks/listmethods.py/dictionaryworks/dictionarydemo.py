# key:value pairs
# dictionary

student=[1000,"ram","django","mca"]

print(student[1])

student={"rol":1000,"name":"ram","course":"django","qualification":"mca"}


# ......nxt....

# employee id=100 name=vipin department salary=25000

employee={"id":100,"name":"vipin","department":"hr","salary":25000}

print(employee["name"]) #indexing not supported

# ........nxt.....

# create a dictonary product with keys id,title,price,brand

product={"id":1000,"title":"goodday","price":35,"brand":"britania"}

print(product["price"])#display product price

# update product price as 45
product["price"]=45

print(product)

product["use_by_date"]="12-10-2024"

print(product)

product["price"]=100

print(Product)

product["offer"]=5

# check key is exit or not
# exist
# not exist

if("price in product"):
    print("exist")
else:
    print("not exist")


    # 
    if "brand" in product:
        print("exist")
    else:
        print("not exist")

    # add  offer as 10  if after exist else add offer as 20

    if "offer" in product:
        product["offer"]=10

    else:
        product["offer"]=20
    print(product) 