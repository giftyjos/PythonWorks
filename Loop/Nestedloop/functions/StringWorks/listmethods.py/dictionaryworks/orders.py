

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
# order_summary
summary_dictionary={}

for item in orders:
    if item in summary_dictionary:
        summary_dictionary[item]+=1
    else:

        summary_dictionary[item]=1
print(summary_dictionary)