f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\countries.json",encoding="uft-8")

data=load(f)

# print number of countries
# print(len(data))

# /print all country names

all_country_names=[country.get("name")for country in data ]
# print(all_country_names)

# print all  regions
all_regions-[country.get("region")for country in data]
# print(set(all_regions))

region_count={region:all_regions.count(region) for region in all_regions}

# print(region_count)

# printing maximum region count

max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count,region_count.get(max_region_count))

# capital of india

country_capital=[coutry.get("captial") for country in data if country.get("name")=="India"]
# print(country_capital)

# countries with most numbers of borders

country_borders={country.get("name"):len(country.get("borders",[])) for country in data}
# print(country_borders)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

country_border_count={}

#[ for country in data:

    # border_count=len(country.get("broder",[]))
    # country_border_count[country.get("name")]=border_count
# print(country_border_count)
# max_region_count=max(country_border_count,key=lambda k:country_border_count)  ]  this is lengthy way molil ullath one line code excute



# most populated country

most_populated_country=max(data,key=lambda country:country.get("populated",0)).get("name")
print(most_populated_country)

# country borders

alpha_three_codes=[country.get("border") for country in data if country.get("name") =="India"]
for code in alpha_three_codes:
    for country in data:
        if country.get("alphathreecode")==code:
         print(country.get("name"))